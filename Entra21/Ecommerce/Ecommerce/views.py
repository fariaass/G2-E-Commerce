from django.shortcuts import render
from categorias.models import Categoria
import requests

def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'categorias': categorias})

