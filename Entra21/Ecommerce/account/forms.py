from account.models import MyUser
from django.forms import ModelForm

class MyUserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ('email', 'nome_usuario', 'primeiro_nome', 'ultimo_nome', 'contato',)