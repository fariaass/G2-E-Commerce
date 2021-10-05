# Generated by Django 3.1.3 on 2021-10-02 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('nome_usuario', models.CharField(max_length=40)),
                ('primeiro_nome', models.CharField(max_length=255)),
                ('ultimo_nome', models.CharField(max_length=255)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('ultimo_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('contato', models.CharField(max_length=11)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=256)),
                ('cep', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=256)),
                ('numero', models.IntegerField(default='')),
                ('tipo', models.CharField(choices=[('A', 'Apartamento'), ('R', 'Residência'), ('C', 'Comercial'), ('O', 'Outro')], default='O', max_length=1)),
                ('bairro', models.CharField(max_length=256)),
                ('cidade', models.CharField(max_length=256)),
                ('estado', models.CharField(max_length=256)),
                ('pais', models.CharField(default='Brasil', max_length=256)),
                ('referencia', models.CharField(default='', max_length=256)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
