from rest_framework import permissions
from .models import RoleChoices


class IsInvestidorOrReadOnly(permissions.BasePermission):
    """
    Se não tiver a permission de ADMIN_SUPER não consegue modificar com os metodos HTTP.
    Usuários autenticados podem fazer leitura do GET, HEAD e OPTIONS.
    """
    def has_permission(self, request, view):
        if not request.user and request.user.is_authenticated:
            return False
        if request.user.role == RoleChoices.ADMIN_SUPER:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == RoleChoices.INVESTIDOR_PLENO:
            return True