from categorias.models import Tag
from categorias.models import Categoria
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializa o modelo de categoria.
    """
    class Meta:
        model = Categoria
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """
    Serializa o modelo de tag.
    """
    class Meta:
        model = Tag
        fields = '__all__'