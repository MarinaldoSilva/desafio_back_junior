from users.models import RoleChoices

class MultiTenantScopeMixin:
    """Mixin para verificar hosts e roles permissions"""
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        
        if not user or not user.is_authenticated:
            return qs.none()
        
        if user.role == RoleChoices.ADMIN_SUPER:
            return qs
        if user.host:
            qs.filter(host=user.host)
        
        return qs.none()
    
    def perform_create(self, serializer):
        serializer.save(
            criado_por=self.request.user,
            host=self.request.user.host
        )