from django.shortcuts import render
from accounts.models import Endereco, MyUser
#from carrinho.models import Carrinho
from produtos.views import search
from Ecommerce.forms import SearchForm
from accounts.forms import EnderecoForm

def retorna_endereco(request):
    dados = Endereco.objects.all()
    return render(request, 'pedidos/endereco.html', {'dados': dados})

def teste_identificacao(request):
    return render(request, 'pedidos/identificacao.html')

def pagamento(request):
    return render(request, 'pedidos/pagamentos.html')