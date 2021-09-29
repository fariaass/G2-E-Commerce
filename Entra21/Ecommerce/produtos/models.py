from categorias.models import Categoria, Tag
from django.db import models
import datetime


class Produto(models.Model):
    """
    Modelo dos produtos com seus respectivos campos.

    Tags tornam a pesquisa mais fácil.
    """
    nome                = models.CharField(max_length=72)
    descricao           = models.TextField()
    preco               = models.DecimalField(max_digits=12, decimal_places=2)
    imagem              = models.FileField(upload_to='media')
    categoria           = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    tags                = models.ManyToManyField(Tag, related_name='produtos')
    data_criacao        = models.DateField(auto_now_add=True)
    visualizacoes       = models.IntegerField()
    vendas              = models.IntegerField()
    is_disponivel       = models.BooleanField(default=True)

    objects = models.Manager()
        
    def __str__(self):
        return self.nome
