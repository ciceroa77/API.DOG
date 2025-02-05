from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100)  # Nome do animal
    species = models.CharField(max_length=50)  # Espécie do animal
    breed = models.CharField(max_length=50)  # Raça do animal
    age = models.IntegerField()  # Idade do animal
    owner_name = models.CharField(max_length=100)  # Nome do dono

    def __str__(self):
        return self.name  # Retorna o nome do animal quando for exibido no admin
