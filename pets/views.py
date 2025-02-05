from rest_framework import viewsets
from .models import Pet
from .serializers import PetSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()  # Todos os pets do banco de dados
    serializer_class = PetSerializer  # Usa o serializer definido
