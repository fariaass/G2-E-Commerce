from django.db import models
from accounts.models import Endereco, MyUser
from produtos.models import Produto

class Pedido(models.Model):

    CHOICES = (
        ('P', 'Pix',),
        ('B', 'Boleto',),
        ('C', 'Crédito',),
    )

    usuario                 = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='pedidos')
    produtos                = models.ManyToManyField(Produto, related_name='pedidos')
    valor                   = models.DecimalField(decimal_places=2, max_digits=15)
    forma_pagamento         = models.CharField(max_length=1, choices=CHOICES)
    endereco                = models.ForeignKey(Endereco, on_delete=models.SET_DEFAULT, default='Excluído', related_name='pedidos')
    quantidade_produtos     = models.JSONField()
    frete                   = models.DecimalField(decimal_places=2, max_digits=9)
    foi_pago                = models.BooleanField(default=False)
