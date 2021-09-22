from django.shortcuts import render
from categorias.models import Categoria
import requests

def home(request):
    categorias = Categoria.objects.all()
    categorias = categoria_queryset_parser(categorias)
    ultimo_item = categorias[-1]
    categorias.pop()
    print(categorias)
    return render(request, 'home.html', {'categorias': categorias, 'ultimo_item': ultimo_item})

def categoria_queryset_parser(query):
    query_parsed = []
    for item in query:
        dic = {'id': item.id, 'nome': item.nome, 'imagem': item.imagem}
        query_parsed.append(dic)
    return query_parsed
