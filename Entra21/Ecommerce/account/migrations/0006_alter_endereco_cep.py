# Generated by Django 3.2.6 on 2021-09-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_delete_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=10),
        ),
    ]