from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from json import loads
from pedidos.forms import PedidoForm
from produtos.models import Produto

def identificacao(request):
    if request.user.is_authenticated:
        if len(request.user.carrinho.produtos.all()) != 0:
            return render(request, 'pedidos/identificacao.html')
        else:
            return render(request, 'erro.html', {'message': 'Seu carrinho está vazio.'})
    else:
        if request.session.get('cart_products', False):
            if request.session['cart_products']:
                return render(request, 'pedidos/identificacao.html')
            else:
                return render(request, 'erro.html', {'message': 'Seu carrinho está vazio.'})
        else:
            return render(request, 'erro.html', {'message': 'Seu carrinho está vazio.'})


@login_required(login_url='/login/')
def pagamento(request):
    return render(request, 'pedidos/pagamentos.html')


def sessiont_cart_to_account_cart(request):
    if request.GET.get('authenticated', False):
        if request.user.is_authenticated:
            products = request.session['cart_products']
            products = [loads(v) for k, v in products.items()]
            products = [p[0] for p in products]
            products = [get_object_or_404(Produto, pk=i['pk']) for i in products]
            [request.user.carrinho.produtos.add(i) for i in products]
            del request.session['cart_products']
        else:
            return render(request, 'erro.html', {'message': 'Usuário não autenticado.'})
    return redirect("/pedidos/identificacao/")

def salva_pedido(request):
    if request.method == 'POST':
        form = PedidoForm()
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.produtos = request.user.carrinho.produtos.all()


def test_js(request):
    print(request.GET)
    return redirect("/carrinho/")