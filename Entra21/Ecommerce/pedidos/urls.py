from django.db import reset_queries
from django.urls import path
from pedidos.views import retorna_endereco, teste_identificacao, pagamento

app_name = 'pedidos'

"""
Urls do app pedidos.
"""

urlpatterns = [
    path('identificacao/', teste_identificacao, name='identificacao'),
    path('endereco/', retorna_endereco, name='endereco'),
    path('pagamento/', pagamento, name='pagamento'),
]