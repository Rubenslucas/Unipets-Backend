from django.contrib import admin
from users.models import UserProfile
from django.contrib.auth.admin import UserAdmin


class UserProfileAdmin(UserAdmin):
    fieldsets = (
        ('Informações do usuário', {'fields': ('username', 'password', 'email', 'name', 'cpf_cnpj', 
        'birthday', 'photo', 'phone', 'city', 'state', 'district', 'address', 'cep')}),
        ('Tipos de usuário', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
        ('Permissões', {'fields': ('groups',)}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ['email','name', 'cpf_cnpj']
    search_fields = ['email', 'name', 'cpf_cnpj']

    
admin.site.register(UserProfile, UserProfileAdmin)