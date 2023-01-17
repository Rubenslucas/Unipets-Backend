from rest_framework.viewsets import ModelViewSet
from .models import Pet
from .serializer import PetSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from datetime import datetime
from rest_framework.generics import CreateAPIView


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], permission_classes=[IsAuthenticated], detail=False)
    def create_pet(self, request):
        user = request.user
        data = request.data
        try:
            pet = Pet.objects.create(
                name=data['name'],
                description=data.get('description'),
                sex=data['sex'],
                age=data['age'],
                species=data['species'],
                breed=data['breed'],
                chip=data.get('chip'),
                donor_id=user.id
            )

            return Response({'message': 'Pet cadastrado com sucesso.'}, status=status.HTTP_200_OK)

        except Exception as error:
            return Response({'messege': 'Erro ao cadastrar o pet.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(methods=['POST'], permission_classes=[IsAuthenticated], detail=False)
    def edit_pet(self, request):
        data = request.data
        try:
            pet = Pet.objects.filter(pk=data['pet_id']).update(
                name=data['name'],
                description=data.get('description'),
                sex=data['sex'],
                age=data['age'],
                species=data['species'],
                breed=data['breed'],
                chip=data.get('chip')
            )

            return Response({'message': 'Pet editado com sucesso.'}, status=status.HTTP_200_OK)

        except Exception as error:
            return Response({'message': 'Falha ao editar pet.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)