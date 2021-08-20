from produtos.models import Produto
from rest_framework.serializers import ModelSerializer

class ProdutoSerializer(ModelSerializer):
    """
    Serializa o modelo de produto.
    """
    class Meta:
        model = Produto
        fields = '__all__'