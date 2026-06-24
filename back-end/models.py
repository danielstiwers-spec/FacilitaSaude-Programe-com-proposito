from django.db import models

class Usuario(models.Model):
    # O Django cria o campo 'id' automaticamente
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=12)
    email = models.EmailField()
    senha = models.CharField(max_length=128) # Guardará a senha com segurança

    def __str__(self):
        return self.email
