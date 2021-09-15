from categorias.models import Categoria, Tag
from django.db import models
import datetime

class DisponivelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_disponivel=True)

class Produto(models.Model):
    """
    Modelo dos produtos com seus respectivos campos.

    Tags tornam a pesquisa mais fácil.
    """
    nome                = models.CharField(max_length=256)
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
    disponivel = DisponivelManager()

    class Meta:
        ordering = ("name",)
        
    def __str__(self):
        return self.nome

    def __gt__(self, other):
        return datetime.date(self.data_criacao) > datetime.date(other.data_criacao)

    def __lt__(self, other):
        return datetime.date(self.data_criacao) < datetime.date(other.data_criacao)

