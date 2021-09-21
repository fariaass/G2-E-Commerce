from produtos.views import recomendacao
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto
from carrinho.models import Carrinho

@login_required
def retorna_carrinho(request, pk):
    """
    O retorno consiste em um template acompanhado de um json com os dados do carrinho.
    """

    # Itens carrinho
    try:
        dados = get_object_or_404(Carrinho, pk=pk)
        produtos = [get_object_or_404(Produto, id=i.id) for i in dados.produtos.all()]

        # total do carrinho
        total_itens = len(produtos)
        total = [i.preco for i in produtos]
        total = sum(total)
        
        return render(request, 'carrinho/carrinho.html', {'dados': produtos, 'total_itens': total_itens, 'total': total, 'no_match': False})
    except:
        no_match = True

    return render(request, 'carrinho/carrinho.html', {'no_match': no_match})


@login_required(login_url='/login/')
def adicionar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    carrinho = get_object_or_404(Carrinho, id=request.user.carrinho.id)
    carrinho.produtos.add(produto)
    reco = recomendacao(Produto.objects.all(), produto)
    return render(request, 'produtos/detalhes_produto.html', {'produto':produto, 'dados':reco, 'nome':'Produto', 'success': True, 'in_cart': True})


@login_required(login_url='/login/')
def remover(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    carrinho = get_object_or_404(Carrinho, id=request.user.carrinho.id)
    carrinho.produtos.remove(produto)
    reco = recomendacao(Produto.objects.all(), produto)
    return render(request, 'produtos/detalhes_produto.html', {'produto':produto, 'dados':reco, 'nome':'Produto', 'success': False, 'in_cart': False})
