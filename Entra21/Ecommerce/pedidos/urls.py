from django.urls import path
from pedidos.views import identificacao, pagamento, sessiont_cart_to_account_cart, inicia_pedido
from accounts.views import retorna_enderecos

app_name = 'pedidos'

"""
Urls do app pedidos.
"""

urlpatterns = [
    path('identificacao/', identificacao, name='identificacao'),
    path('endereco/', retorna_enderecos, name='endereco'),
    path('pagamento/<int:pk>/', pagamento, name='pagamento'),
    path('session-to-account/', sessiont_cart_to_account_cart, name='session-to-account'),
    path('inicia-pedido/', inicia_pedido, name='inicia-pedido'),
]