from django.shortcuts import render
from categorias.models import Categoria
import requests

def home(request):
    categorias = Categoria.objects.all()
    categorias = categoria_queryset_parser(categorias)
    return render(request, 'home.html', {'categorias': categorias})


