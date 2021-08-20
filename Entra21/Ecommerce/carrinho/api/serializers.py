from carrinho.models import Carrinho
from rest_framework.serializers import ModelSerializer

class CarrinhoSerializer(ModelSerializer):
    """
    Serializa o modelo de carrinho.
    """
    class Meta:
        model = Carrinho
        fields = '__all__'