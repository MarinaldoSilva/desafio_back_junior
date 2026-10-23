from rest_framework.viewsets import ModelViewSet
from wallet.mixins import MultiTenantScopeMixin
from users.permissions import IsInvestidorOrReadOnly
from .models import Portfolio
from .serializers import PortfoliSerializer

class PortfolioViewSet(ModelViewSet, MultiTenantScopeMixin):
    queryset = Portfolio.objects.all()
    serializer_class = PortfoliSerializer
    permission_classes = IsInvestidorOrReadOnly
    lookup_field = 'uuid'
    
    
    
