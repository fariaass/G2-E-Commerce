from produtos.views import produto_queryset_parser, recomendacao
from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
from carrinho.models import Carrinho
from json import loads

def retorna_carrinho(request):
    """
    O retorno consiste em um template acompanhado de um json com os dados do carrinho.
    """
    if request.user.is_authenticated:
        dados = get_object_or_404(Carrinho, pk=request.user.carrinho.pk)
        if len(dados.produtos.all()) == 0:
            return render(request, 'carrinho/carrinho.html', {'no_match': True})
        produtos = [get_object_or_404(Produto, id=i.id) for i in dados.produtos.all()]
        # total do carrinho
        total_itens = len(produtos)
        total = [i.preco for i in produtos]
        total = sum(total)
        
        return render(request, 'carrinho/carrinho.html', {'dados': produtos, 'total_itens': total_itens, 'total': total, 'no_match': False})

    else:
        if request.session.get('cart_products', False):
            products = request.session['cart_products']
            if len(products) == 0:
                return render('carrinho/carrinho.html', {'no_match': True})
            products = [loads(p) for p in products]
            products = [p[0] for p in products]
            products = produto_queryset_parser(products, to_session_cart=True)
            total_itens = len(products)
            total = [float(p['preco']) for p in products]
            total = sum(total)
        else:
            return render(request, 'carrinho/carrinho.html', {'no_match': True})
        
        return render(request, 'carrinho/carrinho.html', {'dados': products, 'total_itens': total_itens, 'total': total, 'no_match': False})


def adicionar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.user.is_authenticated:
        carrinho = get_object_or_404(Carrinho, id=request.user.carrinho.id)
        carrinho.produtos.add(produto)
    else:
        if request.session.get('cart_products', False):
            request.session['cart_products'].append(serialize('json', [produto]))
        else:
            request.session['cart_products'] = []
            request.session['cart_products'].append(serialize('json', [produto]))

    reco = recomendacao(Produto.objects.all(), produto)
    return render(request, 'produtos/detalhes_produto.html', {'produto':produto, 'dados':reco, 'nome':'Produto', 'success': True, 'in_cart': True})


def remover(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.user.is_authenticated:
        carrinho = get_object_or_404(Carrinho, id=request.user.carrinho.id)
        carrinho.produtos.remove(produto)
    else:
        try:
            products = request.session['cart_products'][:]
        except:
            request.session['cart_products'] = []
            products = request.session['cart_products'][:]

        products.pop(produto)

    reco = recomendacao(Produto.objects.all(), produto)
    return render(request, 'produtos/detalhes_produto.html', {'produto':produto, 'dados':reco, 'nome':'Produto', 'success': False, 'in_cart': False})
