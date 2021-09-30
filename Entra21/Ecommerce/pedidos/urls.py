from django.db import reset_queries
from django.urls import path
from pedidos.views import retorna_endereco, teste_identificacao

app_name = 'account'

"""
Urls do app account.
"""

urlpatterns = [
    path('endereco/', retorna_endereco, name='endereco'),
    path('identificacao/', teste_identificacao, name='identificacao'),
]