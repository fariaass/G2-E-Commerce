from django.shortcuts import render
from categorias.models import Categoria
from categorias.views import categoria_queryset_parser

def home(request):
    categorias = Categoria.objects.all()
    categorias = categoria_queryset_parser(categorias)
    return render(request, 'home.html', {'categorias': categorias})