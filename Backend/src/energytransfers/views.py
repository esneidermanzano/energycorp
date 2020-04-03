# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from rest_framework.permissions import IsAdminUser, BasePermission
from energytransfers.models import Substation, Transformator


from energytransfers.serializers import (
    SubstationSerializer,
    UpdateSubstationSerializer,
    CreateSubstationSerializer,
    InactivateSubstationSerializer,
    DeleteSubstationSerializer,
    TransformatorSerializer,
    CreateTransformatorSerializer,
    UpdateTransformatorSerializer,
    InactivateTransformatorSerializer,
    DeleteTransformatorSerializer
)

from rest_framework.views import APIView
from rest_framework.response import Response


""" ===================================================
Las siguientes clases verifican si quien consulta una ruta
tiene el cargo para poder hacer dicha consulta.
"""


class AllowAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = Worker.objects.filter(
                user=request.user.id).values('user_type')
            return bool(quey[0]['user_type'] == 1)
        else:
            return False


class AllowManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = Worker.objects.filter(
                user=request.user.id).values('user_type')
            return bool(quey[0]['user_type'] == 2)
        else:
            return False


class AllowOperator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = Worker.objects.filter(
                user=request.user.id).values('user_type')
            return bool(quey[0]['user_type'] == 3)
        else:
            return False

# ========== CRUD para la informacion basica del substation ==========
# Listar todos las substation

class SubstationList(ListAPIView):
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer


# Listar un Substation por id
class SubstationDetail(RetrieveAPIView):
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer


# Crear un Substation
class SubstationCreate(ListCreateAPIView):
    queryset = Substation.objects.all()
    serializer_class = CreateSubstationSerializer


# Actualizar datos de un Substation por id
class SubstationUpdate(UpdateAPIView):
    queryset = Substation.objects.all()
    serializer_class = UpdateSubstationSerializer


# Eliminar Substation
class SubstationDelete(DestroyAPIView):
    queryset = Substation.objects.all()
    serializer_class = DeleteSubstationSerializer

# Inactvar Substation


class SubstationInactivate(UpdateAPIView):
    queryset = Substation.objects.all()
    serializer_class = InactivateSubstationSerializer

# ========== CRUD para la informacion del Transfomator ==========
# Listar todos los Transfomator (anida info basica de usuario)


class TransformatorList(ListAPIView):
    queryset = Transformator.objects.all()
    serializer_class = TransformatorSerializer


# Listar un Transfomator por id
class TransformatorDetail(RetrieveAPIView):
    queryset = Transformator.objects.all()
    serializer_class = TransformatorSerializer


# Crear cliente asignando un Transfomator ya existente
class TransformatorCreate(ListCreateAPIView):
    queryset = Transformator.objects.all()
    serializer_class = TransformatorSerializer


# Actualizar datos de Transfomator por id
class TransformatorUpdate(UpdateAPIView):
    queryset = Transformator.objects.all()
    serializer_class = UpdateTransformatorSerializer

# Eliminar Un Transformator sin afectar usuario


class TransformatorDelete(DestroyAPIView):
    queryset = Transformator.objects.all()
    serializer_class =  DeleteTransformatorSerializer


# Inactvar Transformator


class TransformatorInactivate(UpdateAPIView):
    queryset = Transformator.objects.all()
    serializer_class = InactivateTransformatorSerializer
