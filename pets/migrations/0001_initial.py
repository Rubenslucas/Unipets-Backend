# Generated by Django 4.1.5 on 2023-01-13 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('sex', models.CharField(choices=[('male', 'Macho'), ('female', 'Fêmea')], default='male', max_length=30, verbose_name='Sexo')),
                ('age', models.CharField(max_length=30, verbose_name='Idade')),
                ('species', models.CharField(max_length=30, verbose_name='Espécie')),
                ('breed', models.CharField(max_length=30, verbose_name='Raça')),
                ('chip', models.CharField(blank=True, max_length=30, null=True, verbose_name='Microchip')),
                ('adopted', models.BooleanField(default=False, verbose_name='Já foi adotado?')),
                ('adopter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pets_adopter', to=settings.AUTH_USER_MODEL, verbose_name='Adotante')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets_donor', to=settings.AUTH_USER_MODEL, verbose_name='Doador')),
            ],
        ),
    ]