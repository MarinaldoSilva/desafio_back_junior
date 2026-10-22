from django.db import models
from django.conf import settings
import uuid

class Portfolio(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nome_carteira = models.CharField(
        max_length=100, 
        null=False, 
        blank=False
    )
    criador_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False, 
        blank=False,
        related_name="Portfolio_user",
    )
    host = models.CharField(
        max_length=50,
        db_index=True
    )
    