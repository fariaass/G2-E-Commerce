from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
import requests

def retorna_carrinho(request, pk):
    """
    Esta função retorna os dados da api, obtidos através do consumo da mesma pela url.

    O retorno consiste em um template acompanhado de um json.
    """
    dados = requests.get('http://127.0.0.1:8000/api/carrinho/' + str(pk) + '/')
    dados = dados.json()
    produtos = [get_object_or_404(Produto, id=i) for i in dados['produtos']]
    return render(request, 'carrinho/carrinho.html', {'dados':produtos})