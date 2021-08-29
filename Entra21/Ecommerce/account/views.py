from account.forms import MyUserForm
from django.shortcuts import render
import requests

def retorna_account(request, pk):
    """
    Esta função retorna os dados da api, obtidos através do consumo da mesma pela url.

    O retorno consiste em um template acompanhado de um json.
    """
    dados = requests.get('http://127.0.0.1:8000/api/account/' + pk + '/')
    dados = dados.json()
    return render(request, 'EM ABERTO', {'dados':dados})

def cadastra_user(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'registration/formDoneView.html', {'form':form})
    else:
        form = MyUserForm()
    return render(request, 'registration/form.html', {'form':form})
