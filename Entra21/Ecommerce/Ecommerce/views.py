from django.shortcuts import render
from categorias.models import Categoria
from categorias.views import categoria_queryset_parser
import requests

def home(request):
    categorias = Categoria.objects.all()
    categorias = categoria_queryset_parser(categorias)
    return render(request, 'home.html', {'categorias': categorias})

def categoria_queryset_parser(query):
    query_parsed = []
    for item in query:
        dic = {'id': item.id, 'nome': item.nome, 'imagem': item.imagem}
        query_parsed.append(dic)
    return query_parsed