from django.shortcuts import render
import requests

def home(request):
    categorias = requests.get('http://127.0.0.1:8000/api/categorias/')
    categorias = categorias.json()
    return render(request, 'index.html', {'categorias':categorias})

