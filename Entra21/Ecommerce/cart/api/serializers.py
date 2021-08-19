from cart.models import Cart
from rest_framework.serializers import ModelSerializer

class CartSerializer(ModelSerializer):
    """
    Serialize the product model
    """
    class Meta:
        model = Cart
        fields = '__all__'