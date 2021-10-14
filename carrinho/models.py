from django.db import models
from produtos.models import Produto

class Carrinho(models.Model):
    """
    Modelo de carrinho de compras com seus respectivos campos.

    Um usuário pode ter apenas um carrinho, e um carrinho pode ter apenas um usuário.
    """
    usuario                 = models.OneToOneField("accounts.MyUser", on_delete=models.CASCADE, related_name='carrinho')
    produtos                = models.ManyToManyField(Produto, related_name='carrinho')
    