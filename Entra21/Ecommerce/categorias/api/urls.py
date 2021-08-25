from categorias.api.viewsets import CategoriaViewSet, TagViewSet
from django.urls import path

app_name = 'categorias'

"""
Urls da API.
"""

urlpatterns = [
    path('/tags', TagViewSet.list, name='taglist'),
    path('/categorias', CategoriaViewSet, name='categorialist'),
]