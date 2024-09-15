import requests
import base64
import spacy

# Cargar el modelo en inglés
nlp = spacy.load('en_core_web_sm')

def extract_artist_names(text):
    doc = nlp(text)
    artist_names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
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

    params = {
        "q": name_artista,
        "type": "artist",
        "limit": 1
    }

    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()
    return response_data
