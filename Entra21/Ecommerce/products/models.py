from django.db import models

class Product(models.Model):
    """
    Product model with the respective fields.

    Tags turn the search more easy.
    """
    nome                = models.CharField(max_length=255)
    descricao           = models.CharField(max_length=255)
    preco               = models.DecimalField(max_digits=7, decimal_places=2)
    imgagem             = models.FileField(upload_to='media')
    #tags               = models.ManyToManyField('modelo', related_name='produtos')

    def __str__(self):
        return self.nome