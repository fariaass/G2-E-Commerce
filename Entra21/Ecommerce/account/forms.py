from account.models import Endereco
from account.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('email', 'nome_usuario', 'primeiro_nome', 'ultimo_nome', 'contato')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password is not None and password != password2:
            self.add_error("password2", "Suas senhas devem ser iguais")
        return cleaned_data


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('cep', 'rua', 'bairro', 'cidade', 'estado',)
        