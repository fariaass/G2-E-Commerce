from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from json import loads
from pedidos.forms import PedidoForm
from produtos.models import Produto
from accounts.models import Endereco
from carrinho.models import Carrinho

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
    print(request.session.get('pedido'))
    endereco = get_object_or_404(Endereco, pk=request.session['pedido']['endereco'])
    dados = request.user.carrinho.produtos.all()
    total = request.session['pedido'].get('total')
    frete = request.session['pedido'].get('frete')
    total_final = total + frete
    total_itens = 0
    for i in request.session['pedido']['qtd']:
        total_itens += int(i.get('qtd'))
    return render(request, 'pedidos/pagamentos.html', {'endereco': endereco, 'dados': dados, 'total_itens': total_itens, 'total': total, 'frete': frete, 'total_final': total_final})


def session_cart_to_account_cart(request):
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


def fecha_pedido(request):
    if request.method == 'POST':
        form = PedidoForm()
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.produtos = request.user.carrinho.produtos.all()


def inicia_pedido(request):
    request.session['pedido'] = {}
    dados = []
    dicio = {}
    for k, v in request.POST.items():
        if 'id' in k:
            dicio['id'] = v
        elif 'qtd' in k:
            dicio['qtd'] = v
        elif 'unit' in k:
            dicio['unit'] = v
        elif 'total' in k:
            dicio['total'] = v
            dados.append(dicio)
            dicio = {}
        else:
            frete = v
    
    qtd_produtos = [{get_object_or_404(Produto, id=i['id']).nome: i['id'], 'qtd': i['qtd'], 'preco_unitario': i['unit']} for i in dados]
    total = 0
    for i in dados:
        total += float(i['total'])
    request.session['pedido']['qtd'] = qtd_produtos
    request.session['pedido']['total'] = total
    request.session['pedido']['frete'] = float(frete)
    request.session.modified = True
    print(request.session.get('pedido', False))
    return redirect("/carrinho/")

def continua_pedido(request):
    print(request.session.get('pedido', False))
    endereco = request.GET.get('id')
    request.session['pedido']['endereco'] = endereco
    request.session.modified = True
    return redirect("/pedidos/pagamento/")