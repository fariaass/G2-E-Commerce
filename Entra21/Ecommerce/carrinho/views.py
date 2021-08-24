from django.shortcuts import render
import requests

def retorna_carrinho(request, pk):
    dados = requests.get('http://127.0.0.1:8000/api/carrinho/' + pk + '/')
    dados = dados.json()
    return render(request, 'template', {'dados':dados})