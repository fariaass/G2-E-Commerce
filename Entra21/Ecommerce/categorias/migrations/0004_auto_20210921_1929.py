# Generated by Django 3.1.3 on 2021-09-21 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0003_auto_20210917_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagem',
            field=models.ImageField(default='Ecommerce\\media\\media\x08arbie2.jpg', upload_to='media'),
        ),
        migrations.AddField(
            model_name='tag',
            name='imagem',
            field=models.ImageField(default='Ecommerce\\media\\media\x08arbie2.jpg', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
