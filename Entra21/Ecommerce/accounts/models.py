from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
from carrinho.models import Carrinho

class MyUserManager(BaseUserManager):
    """
    Gerenciador de usuários personalizados que cria e salva usuários e super usuários.
    """
    def create_user(self, email, nome_usuario, primeiro_nome, ultimo_nome, password=None):
        """
        Cria e salva um usuário com o email, nome de usuário, primeiro nome e ultimo nome fornecidos.
        """
        if not email:
            raise ValueError('Usuários devem ter um email')
        if not nome_usuario:
            raise ValueError('Usuários devem ter um nome de usuário')
        if not primeiro_nome:
            raise ValueError('Usuários devem ter um primeiro nome')
        if not ultimo_nome:
            raise ValueError('Usuários devem ter um último nome')

        user = self.model(
            email=self.normalize_email(email),
            nome_usuario=nome_usuario,
            primeiro_nome=primeiro_nome,
            ultimo_nome=ultimo_nome,
        )

        user.set_password(password)
        user.save(using=self._db)
        carrinho = Carrinho()
        carrinho.usuario = user
        carrinho.save()
        return user


    def create_superuser(self, email, nome_usuario, primeiro_nome, ultimo_nome, password=None):
        """
        Cria e salva um super usuário com email, nome de usuário, primeiro nome e último nome fornecidos.
        """
        user = self.create_user(
            email=email,
            password=password,
            nome_usuario=nome_usuario,
            primeiro_nome=primeiro_nome,
            ultimo_nome=ultimo_nome,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    """
    Modelo de usuário personalizado com seus respectivos campos.
    """
    email                   = models.EmailField(verbose_name='email',max_length=60, unique=True)
    nome_usuario            = models.CharField(max_length=40)
    primeiro_nome           = models.CharField(max_length=255)
    ultimo_nome             = models.CharField(max_length=255)
    data_criacao            = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    ultimo_login            = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    contato                 = models.CharField(max_length=11)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_usuario', 'primeiro_nome', 'ultimo_nome']

    def __str__(self):
        return self.nome_usuario


    def has_perm(self, perm, obj=None):
        return self.is_admin


    def has_module_perms(self, app_label):
        return True


class Endereco(models.Model):

    CHOICES = (
        ('A', 'Apartamento',),
        ('R', 'Residência',),
        ('C', 'Comercial',),
        ('O', 'Outro',),
    )

    usuario                 = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='enderecos')
    nome                    = models.CharField(max_length=256, default='')
    cep                     = models.CharField(max_length=10)
    rua                     = models.CharField(max_length=256)
    numero                  = models.IntegerField(default='')
    tipo                    = models.CharField(max_length=1, choices=CHOICES, default='O')
    bairro                  = models.CharField(max_length=256)
    cidade                  = models.CharField(max_length=256)
    estado                  = models.CharField(max_length=256)
    pais                    = models.CharField(max_length=256, default='Brasil')
    referencia              = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.nome


# """
# Cria um token para o novo usuário cadastrado.
# """
# @receiver(post_save, sender=MyUser)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)