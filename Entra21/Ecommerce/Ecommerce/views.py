from django.shortcuts import render
import requests

def home(request):
    categorias = requests.get('htpp:127.0.0.1:8000/api/categorias/')
    categorias = categorias.json()
    return render(request, 'index.html', {'categorias':categorias})

