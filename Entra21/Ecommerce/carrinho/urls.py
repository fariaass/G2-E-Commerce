from django.urls import path
from carrinho.views import retorna_carrinho, adicionar, remover

app_name = 'carrinho'

"""
URLs do app carrinho.
"""

urlpatterns = [
    path('', retorna_carrinho, name='retrieve'),
    path('adicionar/<int:pk>/', adicionar, name='adicionar'),
    path('remover/<int:pk>/', remover, name='remover')
]