from rest_framework import serializers
from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'name', 'email', 'cpf_cnpj', 'birthday', 'photo', 'phone', 'city', 'state', 'district', 'address', 'cep']