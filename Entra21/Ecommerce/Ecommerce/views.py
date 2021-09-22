from django.shortcuts import render
from categorias.models import Categoria
import requests

def home(request):
    categorias = Categoria.objects.all()
    ultimo_item = categorias.pop()
    return render(request, 'home.html', {'categorias': categorias})

