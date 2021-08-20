from rest_framework.response import Response
from carrinho.api.serializers import CarrinhoSerializer
from carrinho.models import Carrinho
from rest_framework.viewsets import ModelViewSet

class CarrinhoViewSet(ModelViewSet):
    serializer_class = CarrinhoSerializer
    queryset = Carrinho.objects.all()

    def list(self, request):
        """
        Esta função retorna o carrinho serializado.
        """
        carrinho = self.queryset
        carrinho = self.serializer_class(carrinho, many=True)
        return Response(carrinho.data)