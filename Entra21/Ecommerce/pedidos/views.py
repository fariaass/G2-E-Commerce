# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login
#from account.forms import MyUserForm, EnderecoForm
from django.shortcuts import get_object_or_404, render
from account.models import Endereco, MyUser
#from carrinho.models import Carrinho
from produtos.views import search
from Ecommerce.forms import SearchForm

def retorna_endereco(request):
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    dados = Endereco.objects.all()
    return render(request, 'pedidos/endereco.html', {'dados': dados, 'form': form})

def teste_identificacao(request):
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    return render(request, 'pedidos/identificacao.html', {'form': form})