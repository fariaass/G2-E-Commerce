from django.db import models

class Categorias(models.Model):
    """
    Modelo de categoria com seus respectivos campos.
    """
    nome                    = models.CharField(max_length=256)
    imagem                  = models.ImageField(upload_to='media/categorias', default='media/barbie2.jpg')

    def __str__(self):
        return self.nome

class Tag(models.Model):
    """
    Modelo de tag com seus respectivos campos.

    Tags tornam a pesquisa mais fácil.
    """
    nome                    = models.CharField(max_length=256)
    imagem                  = models.ImageField(upload_to='media/categorias', default='media/barbie2.jpg')

    def __str__(self):
        return self.nome