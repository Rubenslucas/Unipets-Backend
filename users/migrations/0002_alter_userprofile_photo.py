# Generated by Django 4.1.5 on 2023-01-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users-photos', verbose_name='Foto de perfil'),
        ),
    ]
