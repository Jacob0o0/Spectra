from django.shortcuts import render
from django.http import HttpRequest

def chat(request):
    context = {}

    return render(request, 'chat.html', context=context)