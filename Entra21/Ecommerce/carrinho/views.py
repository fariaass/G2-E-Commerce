from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
from carrinho.models import Carrinho
from produtos.views import produto_queryset_parser
from django.core.serializers import serialize
from json import loads
from produtos.forms import SearchForm
from produtos.views import search

def retorna_carrinho(request):
    """
    Esta função retorna o carrinho em formato json, e confere se o carrinho é de sessão,
    ou se é de um usuário logado.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
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
            if not products:
                return render('carrinho/carrinho.html', {'no_match': True})
            products = [loads(v) for k, v in products.items()]
            products = [p[0] for p in products]
            products = produto_queryset_parser(products, to_session_cart=True)
            total_itens = len(products)
            total = [float(p['preco']) for p in products]
            total = sum(total)
        else:
            return render(request, 'carrinho/carrinho.html', {'no_match': True})

        return render(request, 'carrinho/carrinho.html', {'dados': products, 'total_itens': total_itens, 'total': total, 'no_match': False, 'form': form})    

def adicionar(request, pk):
    """
    Esta função adiciona um item ao carrinho, se o usuário estiver logado, e se não estiver,
    adiciona um item ao carrinho da sessão.
    """
    produto = get_object_or_404(Produto, pk=pk)
    if request.user.is_authenticated:
        carrinho = get_object_or_404(Carrinho, id=request.user.carrinho.id)
        carrinho.produtos.add(produto)
    else:

        if request.session.get('cart_products', False):
            request.session['cart_products'][produto.pk] = serialize('json', [produto])
        else:
            request.session['cart_products'] = {}
            request.session['cart_products'][produto.pk] = serialize('json', [produto])

        request.session.modified = True

    return render(request, 'produtos/detalhes_produto.html', {'produto': produto, 'in_cart': True})


def remover(request, pk):
    """
    Esta função remove um item do carrinho, se o usuário estiver logado, e se não estiver,
    remove um item do carrinho da sessão.
    """
    produto = get_object_or_404(Produto, pk=pk)

    if request.user.is_authenticated:
        carrinho = get_object_or_404(Carrinho, id=request.user.carrinho.id)
        carrinho.produtos.remove(produto)
    else:
        if request.session.get('cart_products', False):
            if request.session['cart_products'].get(str(produto.pk), False):
                request.session['cart_products'].pop(str(produto.pk))
            else:
                return render(request, 'erro.html', {'message': 'Este produto não está no seu carrinho'})
        else:
            request.session['cart_products'] = {}
            return render(request, 'erro.html', {'message': 'Este produto não está no seu carrinho'})

    request.session.modified = True

    if 'carrinho' in request.path:
        return retorna_carrinho(request)

    return render(request, 'produtos/detalhes_produto.html', {'produto': produto, 'in_cart': False})
