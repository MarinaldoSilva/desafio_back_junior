from models import Transaction
from ..holding.models import Holding
from rest_framework.exceptions import ValidationError


class transactionService:
    @classmethod
    def createTransaction(cls, holding:Holding, tipo:str, quantidade:int, preco, user):
        
        if tipo == "COMPRA":
            ...