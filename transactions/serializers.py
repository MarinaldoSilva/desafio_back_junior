from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    model = Transaction
    fields = [
        'quantidade_negociada',
        'preco_unidade',
        'tipo_operacao',
        'criado_por',
        'holding',
        'created_at'
    ]
    read_only_fields =[
        'criado_por',
        'created_at'
    ]
    
    