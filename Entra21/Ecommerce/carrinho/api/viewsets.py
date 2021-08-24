from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from carrinho.api.serializers import CarrinhoSerializer
from carrinho.models import Carrinho
from rest_framework.viewsets import ModelViewSet

class CarrinhoViewSet(ModelViewSet):
    serializer_class = CarrinhoSerializer
    queryset = Carrinho.objects.all()

    def list(self, request):
        """
        Esta função retorna os carrinhos serializados.
        """
        carrinho = self.queryset
        carrinho = self.serializer_class(carrinho, many=True)
        return Response(carrinho.data)

    def retrieve(self, request, pk):
        """
        Esta função retorna o carrinho do usuário, serializado.
        """
        carrinho = get_object_or_404(Carrinho, usuario=pk)
        carrinho = self.serializer_class(carrinho)
        return Response(carrinho.data)