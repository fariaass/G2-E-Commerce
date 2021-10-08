from django import forms
from django.forms.widgets import PasswordInput
from accounts.models import Endereco
from accounts.models import MyUser
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class MyUserForm(ModelForm):
    """
    Este é um formulário personalizado para registro de usuários.
    """
    password1 = forms.CharField(widget=PasswordInput, label='Senha')
    password2 = forms.CharField(widget=PasswordInput, label='Confirme a senha')

    class Meta:
        model = MyUser
        fields = ('email', 'nome_usuario', 'primeiro_nome', 'ultimo_nome', 'contato', 'password1', 'password2',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EnderecoForm(ModelForm):
    """
    Este é um formulário para registro de endereços.
    """
    class Meta:
        model = Endereco
        fields = ('nome', 'cep', 'rua', 'numero', 'tipo', 'bairro', 'cidade', 'estado', 'pais', 'referencia')
