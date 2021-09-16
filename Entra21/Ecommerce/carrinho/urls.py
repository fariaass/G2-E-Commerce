from django.urls import path
from carrinho.views import carrinho_remove, carrinho_add, carrinho_detail

app_name = 'carrinho'

"""
URLs do app carrinho.
"""

urlpatterns = [
    # path('<int:pk>/', car, name='retrieve'),
    path("", carrinho_detail, name="carrinho_detail"),
    path("add/<int:product_id>/", carrinho_add, name="add"),
    path("remove/<int:product_id>/", carrinho_remove, name="remove"),
]
