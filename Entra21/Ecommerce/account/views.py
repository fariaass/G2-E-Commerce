from account.forms import MyUserForm, EnderecoForm
from .models import MyUser
from django.shortcuts import render
import requests

def retorna_account(request, pk):
    """
    Esta função retorna os dados da api, obtidos através do consumo da mesma pela url.

    O retorno consiste em um template acompanhado de um json.
    """
    dados = MyUser.pk()
    return render(request, 'EM ABERTO', {'dados':dados})

def cadastra_user(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
        usuario = form.cleaned_data['primeiro_nome']
        return render(request, 'registration/formDoneView.html', {'usuario':usuario})
    else:
        form = MyUserForm()
    return render(request, 'registration/form.html', {'form':form})

def addEndereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.usuario = request.user
            endereco.save()
        return render(request, 'index.html')
    else:
        form = EnderecoForm()
    return render(request, 'registration/addEndereco.html', {'form':form})
