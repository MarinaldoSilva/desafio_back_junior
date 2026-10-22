from django.db import models

class Holding(models.Model):
    wallet = models.ForeignKey(
        'portifolios.Portfolio', 
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="carteira",
    )
    ativo = models.ForeignKey(
        'assets.Asset', 
        on_delete= models.CASCADE,
        help_text="Ticket"
    )
    quantidade_total = models.DecimalField(
        decimal_places=4, 
        max_digits=14
    )
    preco_medio =  models.DecimalField(
        max_digits=14, 
        decimal_places=4
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["wallet", "ativo"], name="unique_wallet_ativo"
            )
        ]
    
    
    def aplicar_compra(self, quantidade, preco):
        self.quantidade_total += quantidade
        
        
    
    def __str__(self): 
        return f"{self.wallet} - {self.ativo} ({self.quantidade_total})"