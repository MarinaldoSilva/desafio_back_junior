from django.db import models
import uuid

class TipoAtivo(models.TextChoices):
    ACAO = "ACAO", "Ações"
    FUNDO_IMOBILIARIO = "FUNDO_IMOBILIARIO", "Fundos Imobiliários"
    RENDA_FIXA = "RENDA_FIXA", "Renda Fixa"

class Asset(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    ticket = models.CharField(
        max_length=10,
        unique=True
    )
    nome = models.CharField(
        max_length=100,
        null=False, 
        blank=False,
        help_text="Nome descritivo do fundo ou empresa")
    
    tipo_investimento = models.CharField(
        max_length=50,
        choices=TipoAtivo.choices, 
        default=TipoAtivo.RENDA_FIXA
    )
    
    class Meta:
        indexes = [
            models.Index(fields=["ticket"])
        ]