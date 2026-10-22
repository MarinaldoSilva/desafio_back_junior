from rest_framework import serializers
from .models import Portfolio


class PortfoliSerializer(serializers.ModelSerializer):
    model = Portfolio
    fields = ['uuid','criado_por', 'nome_carteira', 'host']
    read_only_fields = ['uuid','criado_por','host']
    