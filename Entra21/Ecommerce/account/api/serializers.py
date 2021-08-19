from account.models import MyUser
from rest_framework.serializers import ModelSerializer

class MyUserSerializer(ModelSerializer):
    """
    Serialize the custom user model
    """
    class Meta:
        model = MyUser
        fields = '__all__'