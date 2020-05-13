from rest_framework.permissions import IsAdminUser, BasePermission
from users.models import Worker

#==============================DEFINIMOS LOS PERMISOS===========================================

class AllowAdmin(BasePermission):
    """Verifica los Permisos para el Trabajador Admin"""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = Worker.objects.filter(
                user=request.user.id).values('user_type')
            return bool(quey[0]['user_type'] == 1)
        else:
            return False

class AllowManager(BasePermission):
    """Verifica los Permisos para el Trabajador Gerente"""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = Worker.objects.filter(
                user=request.user.id).values('user_type')
            return bool(quey[0]['user_type'] == 2)
        else:
            return False

class AllowOperator(BasePermission):
    """Verifica los Permisos para el Trabajador Operador"""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = Worker.objects.filter(
                user=request.user.id).values('user_type')
            return bool(quey[0]['user_type'] == 3)
        else:
            return False

