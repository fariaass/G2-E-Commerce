from produtos.api.viewsets import ProdutoViewSet
from django.urls import path

app_name = 'produtos'

"""
URLs da API.
"""

urlpatterns = [
    path('', ProdutoViewSet.list, name='list'),
]