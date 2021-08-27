from django.shortcuts import render
import requests

def retorna_produtos(request):
    """
    Esta função retorna os dados da api, obtidos através do consumo da mesma pela url.

    O retorno consiste em um template acompanhado de um json.
    """
    dados = requests.get('http://127.0.0.1:8000/api/produtos')
    dados = dados.json()
    return render(request, 'TEMPLATE PRODUTOS', {'dados':dados})

def retorna_produtos_mais_vendidos(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vendidos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """


    def bubblesort(v, n):

        if n < 1:
            return
        
        for i in range(n):
            if v[i].vendas < v[i + 1].vendas:
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp

        bubblesort(v, n - 1)


    dados = requests.get('http://127.0.0.1:8000/api/produtos')
    dados = dados.json()
    maior = list(dados)
    bubblesort(maior, len(maior) - 1)
    return render(request, 'HOLDER', {'dados': maior[:20]})

def retorna_produtos_mais_visualizados(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vistos, na ordem decrescente,
    utilizando os métodos mágicos para fazer comparações entre os produtos e determinar qual tem mais visitas.
    """
    dados = requests.get('http://127.0.0.1:8000/api/produtos')
    dados = dados.json()
    maior = list(dados)
    maior.sort(reverse=True)
    return render(request, 'maisVisitados', {'dados':maior[:20]})