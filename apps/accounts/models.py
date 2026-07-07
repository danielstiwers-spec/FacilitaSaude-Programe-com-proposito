from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
    ]

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True)

    sexo = models.CharField(
        max_length=1,
        choices=SEXO,
        blank=True
    )

    data_nascimento = models.DateField(
        null=True,
        blank=True
    )

    cidade = models.CharField(
        max_length=100,
        blank=True
    )

    estado = models.CharField(
        max_length=2,
        blank=True
    )

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    altura = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )

    tipo_sanguineo = models.CharField(
        max_length=3,
        blank=True
    )

    foto = models.ImageField(
        upload_to="usuarios/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
