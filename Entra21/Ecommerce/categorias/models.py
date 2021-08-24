from django.db import models

class Categoria(models.Model):
    """
    Modelo de categoria com seus respectivos campos.
    """
    nome = models.CharField(max_length=256)

class Tag(models.Model):
    """
    Modelo de tag com seus respectivos campos.

    Tags tornam a pesquisa mais fácil.
    """
    nome = models.CharField(max_length=256)