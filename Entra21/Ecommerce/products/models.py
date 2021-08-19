from django.db import models

class Product(models.Model):
    """
    Product model with the respective fields.

    Tags turn the search more easy.
    """
    name                = models.CharField(max_length=255)
    desc                = models.CharField(max_length=255)
    price               = models.DecimalField(max_digits=7, decimal_places=2)
    img                 = models.FileField(upload_to='media')
    #tags                = models.ManyToManyField('modelo', related_name='produtos')

    def __str__(self):
        return self.nome