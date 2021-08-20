from rest_framework.response import Response
from produtos.api.serializers import ProdutoSerializer
from produtos.models import Produto
from rest_framework.viewsets import ModelViewSet

class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

    def list(self, request):
        """
        Esta função retorna os produtos serializados.
        """
        produtos = self.queryset
        produtos = self.serializer_class(produtos, many=True)
        return Response(produtos.data)