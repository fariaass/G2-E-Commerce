from django.utils.encoding import is_protected_type
from produtos.models import Produto
from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from produtos.serializers import ProdutoSerializer
=======
>>>>>>> teste
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
<<<<<<< HEAD
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
    dados = ProdutoSerializer(Produto, many=True, data=dados)
    if dados.is_valid():
        bubblesort(dados.data, len(dados.data) - 1)
    return render(request, 'produtos/produtos.html', {'dados': dados.data, 'titulo':'Mais Vendidos'})
=======
    dados = Produto.objects.all()
    dados = produto_queryset_parser(dados)
    bubblesort(dados, len(dados) - 1, 'vendas')
    return render(request, 'produtos/produtos.html', {'dados': dados, 'titulo':'Mais Vendidos'})
>>>>>>> teste


def retorna_produtos_mais_visualizados(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vistos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
<<<<<<< HEAD
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
    dados = ProdutoSerializer(Produto, many=True, data=dados)
    if dados.is_valid():
        bubblesort(dados.data, len(dados.data) - 1)
    return render(request, 'produtos/produtos.html', {'dados':dados.data, 'titulo':'Mais Visitados'})
=======
    dados = Produto.objects.all()
    dados = produto_queryset_parser(dados)
    bubblesort(dados, len(dados) - 1, 'visualizacoes')
    return render(request, 'produtos/produtos.html', {'dados':dados, 'titulo':'Mais Visitados'})
>>>>>>> teste


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
<<<<<<< HEAD
    dados = ProdutoSerializer(Produto, many=True, data=dados)
    if dados.is_valid():
        bubblesort(dados.data, len(dados.data) - 1)
    return render(request, 'produtos/produtos.html', {'dados':dados.data, 'titulo':'Lançamentos'})
=======
    dados = produto_queryset_parser(dados)
    bubblesort(dados, len(dados) - 1, 'data_criacao')
    return render(request, 'produtos/produtos.html', {'dados':dados, 'titulo':'Lançamentos'})
>>>>>>> teste


def detalhes_produto(request, pk):
    """
    Esta função retorna os dados do produto selecionado.
    """
    produto = get_object_or_404(Produto, pk=pk)
    dados = Produto.objects.all()
    reco = recomendacao(dados, produto)
<<<<<<< HEAD
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto, 'dados': reco, 'nome': 'Produto   ', 'success':False})
=======
    if produto in request.user.carrinho.produtos.all():
        in_cart = True
    else:
        in_cart = False
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto, 'dados': reco, 'nome': 'Produto', 'success': False, 'in_cart': in_cart})
>>>>>>> teste


def recomendacao(query, exclude):
    recomendacao_list = []
    for _ in range(3):
        reco = query[randint(0, len(query) - 1)]
        if reco not in recomendacao_list and reco.nome != exclude.nome:
            recomendacao_list.append(reco)
    
    return recomendacao_list
<<<<<<< HEAD
=======

def produto_queryset_parser(query):
    query_parsed = []
    for item in query:
        dic = {'id': item.id, 'nome': item.nome, 'descricao': item.descricao, 'preco': item.preco, 'imagem': item.imagem, 'data_criacao': item.data_criacao, 'visualizacoes': item.visualizacoes, 'vendas': item.vendas, 'is_disponivel': item.is_disponivel, 'categoria': item.categoria, 'tags': item.tags}
        query_parsed.append(dic)
    return query_parsed

def bubblesort(v, n, key):
        """
        Esta função é um método de ordenação muito conhecido, onde as informações são comparadas em pares,
        e vão sendo realocadas dependendo do resultado da comparação.
        """
        if n < 1:
            return
        
        for i in range(n):
            if v[i][key] < v[i + 1][key]:
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp

        bubblesort(v, n - 1, key)
>>>>>>> teste
