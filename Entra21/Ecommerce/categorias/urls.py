from django.urls import path
from categorias.views import retorna_produtos_categoria

app_name = 'categorias'

"""
Urls do app categorias.
"""

urlpatterns = [
    path('<int:pk>/produtos/', retorna_produtos_categoria, name='list'),
]