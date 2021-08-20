from account.models import MyUser
from rest_framework.serializers import ModelSerializer

class MyUserSerializer(ModelSerializer):
    """
    Serializa o modelo de usuário personalizado.
    """
    class Meta:
        model = MyUser
        fields = '__all__'