from .models import Transaction
from django.db import transaction
from holding.models import Holding
from users.models import User
from rest_framework.exceptions import ValidationError


class transactionService:
    @classmethod
    def createTransaction(cls, holding:Holding, tipo:str, quantidade:int, preco, user:User):
        
        if holding.wallet.host != user.host or user.role == "ADMIN_SUPER":
            raise ValidationError("error: Carteira não esta vinculado ao seu host.")
        with transaction.atomic():
            quantidade_tt = holding.quantidade_total
            if tipo == Transaction.TipoOperacao.VENDA:
                if quantidade_tt < quantidade:
                    raise ValidationError("error: Quantidade insuficiente para negociação.")
                operacao = quantidade_tt - quantidade
                return operacao
            elif tipo == Transaction.TipoOperacao.COMPRA:
                holding.quantidade_total += quantidade 
            
            holding.save()
            
            return Transaction.objects.create(
                holding=holding, 
                tipo=tipo, 
                quantidade_negociada=quantidade, 
                preco_unidade=preco, 
                criado_por=user
            )   
                
                
                
                
                
                
                
                
                
                
                
                
                     
                
 # 2\. with transaction.atomic():
 # if tipo == Transaction.TipoOperacao.VENDA:
 # # Trava contra Venda a Descoberto 
 # if quantidade &gt; holding.quantidade\_total:
 # raise ValidationError( f"Saldo insuficiente. Você possui {holding.quantidade\_total} ações e tentou vender {quantidade}." ) # Reduz a quantidade mantendo o preço médio intacto 
 # holding.quantidade\_total -= quantidade elif tipo == Transaction.TipoOperacao.COMPRA: # Recalcula o Preço Médio Ponderado custo\_anterior = holding.quantidade\_total \* holding.preco\_medio custo\_novo = quantidade \* preco holding.quantidade\_total += quantidade holding.preco\_medio = (custo\_anterior + custo\_novo) / holding.quantidade\_total # Salva o novo saldo na Holding holding.save() # Cria e retorna o histórico impresso (Transaction) return Transaction.objects.create( holding=holding, tipo=tipo, quantidade\_negociada=quantidade, preco\_unidade=preco, criado\_por=usuario )