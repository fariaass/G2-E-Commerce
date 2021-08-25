from categorias.api.serializers import TagSerializer
from categorias.models import Tag
from rest_framework.response import Response
from categorias.api.serializers import CategoriaSerializer
from categorias.models import Categoria
from rest_framework import viewsets

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Esta função retorna as categorias serializadas.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def list(self, request):
        categorias = self.queryset
        categorias = self.serializer_class(categorias, many=True)
        return Response(categorias.data)


class TagViewSet(viewsets.ModelViewSet):
    """
    Esta função retorna as tags serializadas.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request):
        tags = self.queryset
        tags = self.serializer_class(tags, many=True)
        return Response(tags.data)