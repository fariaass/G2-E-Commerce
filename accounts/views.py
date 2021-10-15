from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from accounts.forms import MyUserForm, EnderecoForm
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import MyUser, Endereco
from carrinho.models import Carrinho
from pedidos.models import Pedido

@login_required(login_url='/login/')
def retorna_account(request, pk):
    """
    O retorno consiste em um template acompanhado das informações do usuário.
    """
    dados = get_object_or_404(MyUser, pk=pk)
    return render(request, 'EM ABERTO', {'dados':dados})


def cadastra_user(request):
    """
    Esta função consiste no cadastro de um novo usuário, logando-o e criando um carrinho para o mesmo.
    """
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            carrinho = Carrinho()
            carrinho.usuario = user
            carrinho.save()
            name = form.cleaned_data['primeiro_nome']
            return render(request, 'registration/formDoneView.html', {'usuario': name})
    else:
        form = MyUserForm()
    return render(request, 'registration/form.html', {'form':form})


@login_required(login_url='/login/')
def addEndereco(request):
    """
    Esta função consiste no cadastro de um novo endereço.
    """
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.usuario = request.user
            endereco.save()
        return redirect(request.GET.get('next'))
    else:
        form = EnderecoForm()
    return render(request, 'registration/addEndereco.html', {'form':form})


def retorna_enderecos(request):
    dados = Endereco.objects.all().filter(usuario=request.user.id)
    return render(request, 'pedidos/endereco.html', {'dados': dados})


@login_required(login_url='/login/')
def remover_endereco(request, pk):
    Endereco.objects.filter(id=pk).delete()
    return redirect(request.GET.get('next'))

@login_required(login_url='/login/')
def retorna_perfil(request):
    enderecos = Endereco.objects.all().filter(usuario=request.user.id)
    pedidos = Pedido.objects.all().filter(usuario=request.user.id)
    if len(enderecos) > 1:
        more_than_one = True
    else:
        more_than_one = False
    return render(request, 'registration/perfil.html', {'enderecos': enderecos, 'pedidos': pedidos, 'more_than_one': more_than_one})
    
