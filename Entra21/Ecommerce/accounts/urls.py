from django.urls import path
from accounts.views import addEndereco, cadastra_user, retorna_account, remover_endereco, retorna_perfil

app_name = 'account'

"""
Urls do app account.
"""

urlpatterns = [
    path('<int:pk>/', retorna_account, name='retrieve'),
    path('cadastrar/', cadastra_user, name='cadastrar'),
    path('cadastrar_endereco/', addEndereco, name='cadastrar_endereco'),
    path('remover_endereco/<int:pk>/', remover_endereco, name='remover_endereco'),
    path('perfil/', retorna_perfil, name='retorna_perfil')
]