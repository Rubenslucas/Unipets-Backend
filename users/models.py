from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField('Nome', max_length=150)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=20, unique=True)
    birthday = models.DateField('Data de nascimento', null=True, blank=True)
    photo = models.ImageField('Foto de perfil', upload_to='users-photos', null=True, blank=True)
    phone = models.CharField('Telefone', max_length=30)
    city = models.CharField('Cidade', max_length=150)
    state = models.CharField('Estado', max_length=150)
    district = models.CharField('Bairro', max_length=150)
    address = models.CharField('Endereço', max_length=150)
    cep = models.CharField('CEP', max_length=30)

    
    

