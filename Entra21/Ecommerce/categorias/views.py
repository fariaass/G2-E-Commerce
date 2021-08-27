from django.shortcuts import render
import requests

def retorna_categoria(request, pk):
    dados = requests.get('http://127.0.0.1:8000/api/categorias/' + pk + '/')
    dados = dados.json()
    return render(requests, 'EM ABERTO', {'dados':dados})