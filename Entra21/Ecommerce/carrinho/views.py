from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
from carrinho.models import Carrinho

def retorna_carrinho(request, pk):
    """
    O retorno consiste em um template acompanhado de um json com os dados do carrinho.
    """

    # Itens carrinho

    dados = get_object_or_404(Carrinho, pk=pk)
    produtos = [get_object_or_404(Produto, id=i) for i in dados['produtos']]

    # total do carrinho
    total_itens = len(list(dados))
    total = [i.preco for i in produtos]
    total = sum(total)

    return render(request, 'carrinho/carrinho.html', {'dados': produtos, 'total_itens': total_itens, 'total': total})