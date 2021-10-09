from django.urls import path
from pedidos.views import identificacao, pagamento, sessiont_cart_to_account_cart, test_js
from accounts.views import retorna_enderecos

app_name = 'pedidos'

"""
Urls do app pedidos.
"""

urlpatterns = [
    path('identificacao/', identificacao, name='identificacao'),
    path('endereco/', retorna_enderecos, name='endereco'),
    path('pagamento/', pagamento, name='pagamento'),
    path('session-to-account/', sessiont_cart_to_account_cart, name='session-to-account'),
    path('teste/', test_js, name='teste')
]