from rest_framework.generics import get_object_or_404
from account.models import MyUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import MyUserSerializer

class MyUserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def list(self, request):
        """
        Esta função retorna os usuários serializados.
        """
        users = self.queryset
        users = self.serializer_class(users, many=True)
        return Response(users.data)

    def retrieve(self, request, pk):
        user = get_object_or_404(MyUser, pk=pk)
        user = self.serializer_class(user)
        return Response(user.data)