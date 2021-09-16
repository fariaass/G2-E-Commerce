from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .cart import Carrinho
from .forms import CarrinhoAddProdutoForm


@require_POST
def carrinho_add(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)

    form = CarrinhoAddProdutoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carrinho.add(
            produto=produto, quantity=cd["quantidade"], override_quantity=cd["override"]
        )

    return redirect("carrinho:detail")


@require_POST
def carrinho_remove(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remove(produto)
    return redirect("carrinho:detail")


def carrinho_detail(request):
    carrinho = Carrinho(request)
    return render(request, "carrinho/carrinho_detail.html", {"carrinho": carrinho})


