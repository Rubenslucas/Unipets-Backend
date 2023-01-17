from rest_framework.viewsets import ModelViewSet
from .models import UserProfile
from .serializer import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from datetime import datetime


class UserViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], permission_classes=[AllowAny], detail=False)
    def sign_up(self, request):
        data = request.data
        try:
            if UserProfile.objects.filter(username=data['username']):
                return Response({'message': 'Já existe um usuário com o username informado.'}, status=status.HTTP_409_CONFLICT)

            elif UserProfile.objects.filter(email=data['email']):
                return Response({'message': 'Já existe um usuário com o email informado.'}, status=status.HTTP_409_CONFLICT)

            elif UserProfile.objects.filter(cpf_cnpj=data['cpf_cnpj']):
                return Response({'message': 'Já existe um usuário com o cpf_cnpj informado.'}, status=status.HTTP_409_CONFLICT)


            birthday = datetime.strptime(data['birthday'], "%d/%m/%Y")

            user = UserProfile.objects.create(
               username=data['username'],
               email=data['email'],
               cpf_cnpj=data['cpf_cnpj'],
               birthday=birthday.date(),
               phone=data['phone'],
               city=data['city'],
               state=data['state'],
               district=data['district'],
               address=data['address'],
               cep=data['cep'],
               is_active=False
            )
            
            user.set_password(data['password'])
            user.save()

            return Response({'message': 'Confirme seu email para fazer login.'}, status=status.HTTP_200_OK)

        except Exception as error:
            return Response({'message': 'Falha ao realizar cadastro.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(methods=['POST'], permission_classes=[IsAuthenticated], detail=False)
    def user_edit(self, request):
        user = request.user
        data = request.data
        try:
            birthday = datetime.strptime(data['birthday'], "%d/%m/%Y")

            user = UserProfile.objects.filter(pk=user.id).update(
               email=data['email'],
               birthday=birthday.date(),
               phone=data['phone'],
               city=data['city'],
               state=data['state'],
               district=data['district'],
               address=data['address'],
               cep=data['cep']
            )
        
            return Response({'message': 'Usuário editado com sucesso.'}, status=status.HTTP_200_OK)
            
        except Exception as error:
            return Response({'message': 'Falha ao editar usuário.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        