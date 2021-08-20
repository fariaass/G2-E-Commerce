from django.shortcuts import render
import requests

def retorna_produtos(request):
    """
    Esta função retorna os dados da api, obtidos através do consumo da mesma pela url.

    O retorno consiste em um template acompanhado de um json.
    """
    dados = requests.get('http://127.0.0.1:8000/api/produtos')
    dados = dados.json()
    return render(request, 'EM ABERTO', {'dados':dados})