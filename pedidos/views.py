from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from json import loads
from produtos.models import Produto
from accounts.models import Endereco
from pedidos.models import Pedido

def identificacao(request):
    """
    Esta função confere se o carrinho está vazio ou não, tanto o da sessão quanto o carrinho quando está logado,
    e então retorna o template pro usuário se identificar. Se o carrinho estiver vazio, retornará um template de erro.
    """
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
    """
    Esta função retorna pega o total, o frete, o endereço e a quantidade de produtos, e então retorna o template para selecionar o modo de pagamento.
    """
    endereco = get_object_or_404(Endereco, pk=request.session['pedido'].get('endereco'))
    dados = request.user.carrinho.produtos.all()
    total = request.session['pedido'].get('total')
    frete = request.session['pedido'].get('frete')
    total_final = total + frete
    total_itens = 0
    for i in request.session['pedido'].get('qtd'):
        total_itens += int(i.get('qtd'))
    return render(request, 'pedidos/pagamentos.html', {'endereco': endereco, 'dados': dados, 'total_itens': total_itens, 'total': total, 'frete': frete, 'total_final': total_final})


def session_cart_to_account_cart(request):
    """
    Esta função pega todos os itens presentes no carrinho da sessão e passa para o carrinho do usuário logado.
    Caso o usuário não esteja logado, é retornado um template de erro.
    """
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


@login_required(login_url='/login/')
def finaliza_pedido(request, fm):
    """
    Esta função pega o numero enviado, confere qual a forma de pagamento, se não existe retorna um template de erro,
    e se existe, pega todas as informações, cria um modelo de pedido e salva. Ao salvar, o carrinho e a sessão são limpos.
    """
    print("finaliza pedido")
    fms = {1:'B', 2:'P', 3:'C'}
    if fms.get(fm, False):
        endereco = get_object_or_404(Endereco, id=request.session['pedido'].get('endereco'))
        pedido = Pedido.objects.create(usuario=request.user, valor=request.session['pedido'].get('total'), forma_pagamento=fms.get(fm), endereco=endereco, quantidade_produtos=request.session['pedido'].get('qtd'), frete=request.session['pedido'].get('frete'))
        [pedido.produtos.add(i.id) for i in request.user.carrinho.produtos.all()]
        pedido.save()
        request.user.carrinho.produtos.clear()
        del request.session['pedido']
    else:
        return render(request, 'erro.html', {'message': 'Pagina não encontrada.'})
    return redirect("/")


def inicia_pedido(request):
    """
    Cria uma nova chave no dicionário da sessão, então preenche com outro dicionário, contendo informações sobre os produtos,
    como frete, quantidade, preço unitário, preço total e preço total de todos os produtos.
    A cada nova alteração no template, o ajax dispara um POST para esta função.
    """
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
    """
    Esta função pega o pedido já existente na sessão e complementa com o id do endereço escolhido.
    """
    endereco = request.GET.get('id')
    request.session['pedido']['endereco'] = endereco
    request.session.modified = True
    return redirect("/pedidos/pagamento/")

def confirmacao_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if pedido.foi_pago == True:
        msg = 'Pago'
    else:
        msg = 'Não pago'
    return render(request, 'pedidos/confirmacao.html', {'mensagem': msg})