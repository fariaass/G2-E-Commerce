from rest_framework.response import Response
from products.api.serializers import ProductSerializer
from products.models import Product
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request):
        """
        This function returns the products serialized.
        """
        products = self.queryset
        products = self.serializer_class(products, many=True)
        return Response(products.data)