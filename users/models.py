from django.db import models
from django.contrib.auth.models import AbstractUser


class RoleChoices(models.TextChoices):
    
    INVESTIDOR_JR = "investidor_jr", "Investidor Júnior"
    INVESTIDOR_PLENO = "investidor_pleno", "Investidor Pleno"
    ADMIN_SUPER = "ADMIN_SUPER", "Adm Geral"

class User(AbstractUser):
    
    role = models.CharField(
        max_length=100,
        choices=RoleChoices, 
        default=RoleChoices.INVESTIDOR_JR
    )
    
    host = models.CharField(
        max_length=50,
        null=False, 
        blank=False
    )
    
    def __str__(self):
        return f"Usuário {self.username}"