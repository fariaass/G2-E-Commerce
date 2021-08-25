from categorias.api.viewsets import CategoriaViewSet, TagViewSet
from django.urls import path

app_name = 'categorias'

"""
Urls da API.
"""

urlpatterns = [
    path('', TagViewSet.list, name='taglist'),
    path('', CategoriaViewSet, name='categorialist'),
]