from django.contrib import admin
from django.urls import path, include
from transactions.views import TransactionViewSet
from portifolios.views import PortfolioViewSet 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet, basename='portfolio')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
