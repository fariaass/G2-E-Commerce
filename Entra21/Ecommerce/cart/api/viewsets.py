from rest_framework.response import Response
from cart.api.serializers import CartSerializer
from cart.models import Cart
from rest_framework.viewsets import ModelViewSet

class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def list(self, request):
        """
        This function returns the carts serialized.
        """
        cart = self.queryset
        cart = self.serializer_class(cart, many=True)
        return Response(cart.data)