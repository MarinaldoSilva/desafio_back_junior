from django.db import models
from django.conf import settings

class Transaction(models.Model):
    
    class TipoOperacao(models.TextChoices):
        COMPRA = "COMPRA","Compra"
        VENDA = "VENDA", "Venda"
    
    quantidade_negociada = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        help_text="Quantidade de transações de ativos"
    )
    preco_unidade = models.DecimalField(
        max_digits=14,
        decimal_places=4,
    )
    tipo_operacao = models.CharField(
        max_length=10,
        choices=TipoOperacao, 
        default=TipoOperacao.COMPRA
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Data da transação"
    )
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    holding = models.ForeignKey(
        'holding.Holding', 
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    
