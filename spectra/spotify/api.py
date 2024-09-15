import re
import requests
import base64
import spacy
import random

# Cargar el modelo en inglés
nlp = spacy.load('en_core_web_sm')

# Carga del modelo de PLN
nlp = spacy.load('en_core_web_sm')

# Lista opcional de nombres de bandas comunes
known_bands = ["ACDC", "Led Zeppelin", "The Beatles", "Nirvana", "Pink Floyd", "Radiohead", "Daft punk"]

def extract_artist_names(text):
    doc = nlp(text)
    
    # Extraer nombres de personas o organizaciones usando PLN
    artist_names = [ent.text for ent in doc.ents if ent.label_ in ('PERSON', 'ORG')]
    
    # Expresión regular para buscar posibles nombres de bandas en mayúsculas
    potential_bands = re.findall(r'\b[A-Z][A-Z]+\b(?:\s[A-Z][A-Z]+)*', text)

    # Añadir los nombres de bandas conocidos y cualquier banda detectada por la expresión regular
    artist_names += [band for band in potential_bands if band not in artist_names]

    # Comprobar también si alguna banda conocida está presente en el texto
    for band in known_bands:
        if band in text and band not in artist_names:
            artist_names.append(band)

    return artist_names

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    client_id = "516360b78d1c4691bd65f4aaa5edbb79"
    client_secret = "692359d9c3e740d68f51c1845dce36c1"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    return response_data.get("access_token")

def get_top_tracks_by_artist(artist):
    access_token = get_access_token()
    url = f"https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    name_artista = extract_artist_names(artist)

    # Verifica si la lista está vacía
    if not name_artista:
        print("La lista está vacía.")
    else:
        select_artist = random.choice(name_artista)

        params = {
            "q": select_artist,
            "type": "artist",
            "limit": 1
        }

        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()

        artist = response_data['artists']['items'][0]

        id_artist = artist['id']
        name_artist = artist['name']
        img_artist = artist['images'][0]['url']

        url = f'https://api.spotify.com/v1/artists/{id_artist}/top-tracks'
        top_tracks = requests.get(url, headers=headers)
        top_tracks_data = top_tracks.json()

        tracks = []
        for track in top_tracks_data['tracks']:
            track_json = {}
            track_json['album_name'] = track['album']['name']
            track_json["album_img"] = track['album']['images'][0]["url"]
            track_json["uri"] = track['uri']
            track_json['track_name'] = track['name']
            tracks.append(track_json)

        # Aquí puedes procesar el mensaje como lo necesites
        recomendation_data = {
            'name_artist': name_artist,  # Agregada la coma aquí
            'img_artist': img_artist,
            'tracks': tracks
        }

        return recomendation_data
