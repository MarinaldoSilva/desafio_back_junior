from rest_framework import viewsets, status
from rest_framework.response import Response
from wallet.mixins import MultiTenantScopeMixin
from users.permissions import IsInvestidorOrReadOnly
from .models import Transaction
from .serializers import TransactionSerializer
from .transactionService import transactionService


class TransactionViewSet(MultiTenantScopeMixin, viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = IsInvestidorOrReadOnly
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        transaction = transactionService.createTransaction(
            holding = serializer.validated_data['holding'],
            preco= serializer.validated_data['preco'],
            quantidade= serializer.validated_data['quantidade'],
            tipo= serializer.validated_data['tipo'],
            user= request.user
        )
        return Response(
            self.get_serializer(transaction).data,
            status=status.HTTP_201_CREATED
        )