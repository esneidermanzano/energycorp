from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Banck

from .serializers import (
    # CRUD SERIALIZERS
    BanckSerializer,
    UpdateBanckSerializer,
    CreateBanckSerializer,
    InactivateBanckSerializer,
    DeleteBanckSerializer

    # QUERY SERIALIZERS
)

from .permissions import (
    AllowAdmin,
    AllowManager,
    AllowOperator
)

from rest_framework.views import APIView
from rest_framework.response import Response

# ============================================Views para el modúlo Banck==========================

#----------------------------------------------------Banck------------------------------------------                                      

#                                                       CRUD


class BanckCreate(ListCreateAPIView):
    """View para crear una Subestacion"""
    queryset = Banck.objects.all()
    serializer_class = CreateBanckSerializer

class BanckDetail(RetrieveAPIView):
    """View para retrive una Subestacion""" 
    queryset = Banck.objects.all()
    serializer_class = BanckSerializer

class BanckList(ListAPIView):
    """View para retrive todas las Subestaciones"""
    queryset = Banck.objects.all()
    serializer_class = BanckSerializer

class BanckUpdate(UpdateAPIView):
    """View para update una Subestacion"""
    queryset = Banck.objects.all()
    serializer_class = UpdateBanckSerializer

class BanckDelete(DestroyAPIView):
    """View para delete una Subestacion"""
    queryset = Banck.objects.all()
    serializer_class = DeleteBanckSerializer

class BanckInactivate(UpdateAPIView):
    """View para delete una Subestacion"""
    queryset = Banck.objects.all()
    serializer_class = InactivateBanckSerializer

#                                                   QUERY
