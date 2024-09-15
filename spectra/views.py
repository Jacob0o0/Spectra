from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse

import spectra.bot.spectra_bot
import spectra.spotify
import spectra.spotify.api

def chat(request):
    context = {}

    return render(request, 'chat.html', context=context)

def handle_message(request):
    if request.method == 'POST':
        # Obtener el mensaje del cuerpo de la solicitud
        message = request.POST.get('message')
        
        # Aquí puedes procesar el mensaje como lo necesites
        response_data = {
            'response': f"Mensaje recibido: {message}"
        }

        respuesta = spectra.bot.spectra_bot.interaction(message)
        response_data['respuesta_bot'] = respuesta
        
        return JsonResponse(response_data)

def top_tracks_view(request, artist):
    tracks = spectra.spotify.api.get_top_tracks_by_artist(artist)
    return JsonResponse({"tracks": tracks})
