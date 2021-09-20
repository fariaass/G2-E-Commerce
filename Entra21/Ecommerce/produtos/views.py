from produtos.models import Produto
from django.shortcuts import render, get_object_or_404
from produtos.serializers import ProdutoSerializer
from .models import Produto
from random import randint
from datetime import date, datetime

def retorna_produtos(request):
    """
    Retorna os objetos do modelo Produto.
    """
    dados = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'dados':dados})


def retorna_produtos_mais_vendidos(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vendidos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
    def bubblesort(v, n):
        """
        Esta função é um método de ordenação muito conhecido, onde as informações são comparadas em pares,
        e vão sendo realocadas dependendo do resultado da comparação.
        """
        if n < 1:
            return
        
        for i in range(n):
            if v[i].vendas < v[i + 1].vendas:
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp

        bubblesort(v, n - 1)
    dados = Produto.objects.all()
    bubblesort(dados, len(dados) - 1)
    return render(request, 'produtos/produtos.html', {'dados': dados, 'titulo':'Mais Vendidos'})


def retorna_produtos_mais_visualizados(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vistos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
    def bubblesort(v, n):
        """
        Esta função é um método de ordenação muito conhecido, onde as informações são comparadas em pares,
        e vão sendo realocadas dependendo do resultado da comparação.
        """
        if n < 1:
            return
        
        for i in range(n):
            if v[i].visualizacoes < v[i + 1].visualizacoes:
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp

        bubblesort(v, n - 1)
    dados = Produto.objects.all()
    bubblesort(dados, len(dados) - 1)
    return render(request, 'produtos/produtos.html', {'dados':dados, 'titulo':'Mais Visitados'})


def retorna_produtos_mais_recentes(request):
    """
    Esta função retorna um vetor com os 20 produtos mais recentes cadastrados no banco de dados,
    utilizando os métodos mágicos na classe Produto para fazer a comparação entre as datas,
    essas comparações sendo feitas utilizando a biblioteca datetime.
    """
    def bubblesort(v, n):
        """
        Esta função é um método de ordenação muito conhecido, onde as informações são comparadas em pares,
        e vão sendo realocadas dependendo do resultado da comparação.
        """
        if n < 1:
            return
            
        for i in range(n):
            data_1 = str(v[i].data_criacao).split('-')
            data_2 = str(v[i + 1].data_criacao).split('-')
            if date(data_1[0], data_1[1], data_1[2]) < date(data_2[0], data_2[1], data_2[2]):
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp

        bubblesort(v, n - 1)
    
    dados = Produto.objects.all()
    dados = ProdutoSerializer(Produto, many=True, data=dados)
    if dados.is_valid():
        bubblesort(dados.data, len(dados.data) - 1)
    return render(request, 'produtos/produtos.html', {'dados':dados.data, 'titulo':'Lançamentos'})


def detalhes_produto(request, pk):
    """
    Esta função retorna os dados do produto selecionado.
    """
    produto = get_object_or_404(Produto, pk=pk)
    dados = Produto.objects.all()
    reco = recomendacao(dados, produto)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto, 'dados': reco, 'nome': 'Produto   ', 'success':False})


def recomendacao(query, exclude):
    recomendacao_list = []
    for _ in range(3):
        reco = query[randint(0, len(query) - 1)]
        if reco not in recomendacao_list and reco.nome != exclude.nome:
            recomendacao_list.append(reco)
    
    return recomendacao_list
