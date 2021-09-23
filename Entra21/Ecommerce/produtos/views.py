from produtos.models import Produto
from django.shortcuts import render, get_object_or_404
from .models import Produto
from random import randint

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
    dados = Produto.objects.all()
    dados = produto_queryset_parser(dados)
    bubblesort(dados, len(dados) - 1, 'vendas')
    return render(request, 'produtos/produtos.html', {'dados': dados, 'titulo':'Mais Vendidos'})


def retorna_produtos_mais_visualizados(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vistos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
    dados = Produto.objects.all()
    dados = produto_queryset_parser(dados)
    bubblesort(dados, len(dados) - 1, 'visualizacoes')
    return render(request, 'produtos/produtos.html', {'dados':dados, 'titulo':'Mais Visitados'})


def retorna_produtos_mais_recentes(request):
    """
    Esta função retorna um vetor com os 20 produtos mais recentes cadastrados no banco de dados,
    utilizando os métodos mágicos na classe Produto para fazer a comparação entre as datas,
    essas comparações sendo feitas utilizando a biblioteca datetime.
    """
    dados = Produto.objects.all()
    dados = produto_queryset_parser(dados)
    bubblesort(dados, len(dados) - 1, 'data_criacao')
    return render(request, 'produtos/produtos.html', {'dados':dados, 'titulo':'Lançamentos'})


def detalhes_produto(request, pk):
    """
    Esta função retorna os dados do produto selecionado.
    """
    produto = get_object_or_404(Produto, pk=pk)
    dados = Produto.objects.all()
    reco = recomendacao(dados, produto)
    if request.user.is_authenticated:
        try:
            if produto in request.user.carrinho.produtos.all():
                in_cart = True
            else:
                in_cart = False
        except:
            in_cart = False
    else:
        try: 
            products = request.session['cart_products']
        except:
            in_cart = False
        else:
            if produto in products:
                in_cart = True
            else:
                in_cart = False

    return render(request, 'produtos/detalhes_produto.html', {'produto': produto, 'dados': reco, 'nome': 'Produto', 'success': False, 'in_cart': in_cart})


def recomendacao(query, exclude):
    recomendacao_list = []
    for _ in range(3):
        reco = query[randint(0, len(query) - 1)]
        if reco not in recomendacao_list and reco.nome != exclude.nome:
            recomendacao_list.append(reco)
    
    return recomendacao_list

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
