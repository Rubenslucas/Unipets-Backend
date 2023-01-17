from django.db import models
from users.models import UserProfile


class Pet(models.Model):
    SEX = (
        ('male', 'Macho'),
        ('female', 'Fêmea')
    )

    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', null=True, blank=True)
    sex = models.CharField('Sexo', max_length=30, choices=SEX, default='male')
    age = models.CharField('Idade', max_length=30)
    species = models.CharField('Espécie', max_length=30)
    breed = models.CharField('Raça', max_length=30)
    chip = models.CharField('Microchip', max_length=30, null=True, blank=True)
    donor = models.ForeignKey(UserProfile, verbose_name='Doador', related_name='pets_donor', on_delete=models.CASCADE)
    adopter = models.ForeignKey(UserProfile, verbose_name='Adotante', related_name='pets_adopter', on_delete=models.SET_NULL, null=True, blank=True)
    adopted = models.BooleanField('Já foi adotado?', default=False)

    def __str__(self):
        return f'{self.name}'