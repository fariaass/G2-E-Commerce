from django.urls import path
from carrinho.views import retorna_carrinho

app_name = 'carrinho'

"""
URLs do app carrinho.
"""

urlpatterns = [
    path('<int:pk>/', retorna_carrinho, name='retrieve')
]