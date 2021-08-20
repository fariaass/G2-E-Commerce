from carrinho.api.viewsets import CarrinhoViewSet
from django.urls import path

app_name = 'carrinho'

"""
URLs da API.
"""

urlpatterns = [
    path('', CarrinhoViewSet.list, name='list')    
]