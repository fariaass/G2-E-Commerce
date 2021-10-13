from django.urls import path
from pedidos.views import identificacao, pagamento, session_cart_to_account_cart, inicia_pedido, continua_pedido, finaliza_pedido, confirmacao_pedido
from accounts.views import retorna_enderecos

app_name = 'pedidos'

"""
Urls do app pedidos.
"""

urlpatterns = [
    path('identificacao/', identificacao, name='identificacao'),
    path('endereco/', retorna_enderecos, name='endereco'),
    path('pagamento/', pagamento, name='pagamento'),
    path('session-to-account/', session_cart_to_account_cart, name='session-to-account'),
    path('inicia-pedido/', inicia_pedido, name='inicia-pedido'),
    path('continua-pedido/', continua_pedido, name='continua-pedido'),
    path('finaliza-pedido/<int:fm>/', finaliza_pedido, name='finaliza-pedido'),
    path('confirmacao/', confirmacao_pedido, name='confirmacao')
]