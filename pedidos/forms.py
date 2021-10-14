from django import forms
from pedidos.models import Pedido

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ('forma_pagamento', 'endereco')