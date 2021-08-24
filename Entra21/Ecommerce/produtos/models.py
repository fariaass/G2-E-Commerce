from categorias.models import Categoria, Tag
from django.db import models

class Produto(models.Model):
    """
    Modelo dos produtos com seus respectivos campos.

    Tags tornam a pesquisa mais fácil.
    """
    nome                = models.CharField(max_length=256)
    descricao           = models.CharField(max_length=256)
    preco               = models.DecimalField(max_digits=7, decimal_places=2)
    imagem              = models.FileField(upload_to='media')
    categoria           = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    tags                = models.ManyToManyField(Tag, related_name='produtos')

    def __str__(self):
        return self.nome