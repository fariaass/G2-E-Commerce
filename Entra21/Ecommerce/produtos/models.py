from django.db import models

class Produto(models.Model):
    """
    Modelo dos produtos com seus respectivos campos.

    Tags tornam a pesquisa mais fácil.
    """
    nome                = models.CharField(max_length=255)
    descricao           = models.CharField(max_length=255)
    preco               = models.DecimalField(max_digits=7, decimal_places=2)
    imagem              = models.FileField(upload_to='media')
    #tags               = models.ManyToManyField('modelo', related_name='produtos')

    def __str__(self):
        return self.nome