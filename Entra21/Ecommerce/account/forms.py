from account.models import Endereco
from account.models import MyUser
from django import forms

class MyUserForm(forms.ModelForm):

    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'nome_usuario', 'primeiro_nome', 'ultimo_nome', 'contato')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Suas senhas devem ser iguais")
        return cleaned_data


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('cep', 'rua', 'bairro', 'cidade', 'estado',)
        