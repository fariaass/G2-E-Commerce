from django.urls import path
from account.views import addEndereco, cadastra_user, retorna_account, retorna_endereco

app_name = 'account'

"""
Urls do app account.
"""

urlpatterns = [
    path('<int:pk>/', retorna_account, name='retrieve'),
    path('cadastrar/', cadastra_user, name='cadastrar'),
    path('cadastrar_endereco/', addEndereco, name='cadastrar_endereco'),
    path('endereco/', retorna_endereco, name='endereco')
]