from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import (
    Commercial,
    CommercialInvoice
    )

from .serializers import (
    # CRUD SERIALIZERS
    CommercialSerializer,
    UpdateCommercialSerializer,
    CreateCommercialSerializer,
    InactivateCommercialSerializer,
    DeleteCommercialSerializer,

    CommercialInvoiceSerializer,
    CreateCommercialInvoiceSerializer,
    UpdateCommercialInvoiceSerializer,
    DeleteCommercialInvoiceSerializer
    
    # QUERY SERIALIZERS
)

from .permissions import (
    AllowAdmin,
    AllowManager,
    AllowOperator
)

from rest_framework.views import APIView
from rest_framework.response import Response

# ============================================Views para el modúlo de  publicidad==========================

#----------------------------------------------------publicidad-------------------------------------                                      

#                                                       CRUD

class CommercialCreate(ListCreateAPIView):
    """View para crear una Subestacion"""
    queryset = Commercial.objects.all()
    serializer_class = CreateCommercialSerializer

class CommercialDetail(RetrieveAPIView):
    """View para retrive una Subestacion""" 
    queryset = Commercial.objects.all()
    serializer_class = CommercialSerializer

class CommercialList(ListAPIView):
    """View para retrive todas las Subestaciones"""
    queryset = Commercial.objects.all()
    serializer_class = CommercialSerializer

class CommercialUpdate(UpdateAPIView):
    """View para update una Subestacion"""
    queryset = Commercial.objects.all()
    serializer_class = UpdateCommercialSerializer

class CommercialDelete(DestroyAPIView):
    """View para delete una Subestacion"""
    queryset = Commercial.objects.all()
    serializer_class = DeleteCommercialSerializer

class CommercialInactivate(UpdateAPIView):
    """View para delete una Subestacion"""
    queryset = Commercial.objects.all()
    serializer_class = InactivateCommercialSerializer

#                                                   QUERY

#------------------------------------------------CommercialInvoice-------------------------------------

#                                                   CRUD

class CommercialInvoiceCreate(ListCreateAPIView):
    """View para delete un CommercialInvoice"""
    queryset = CommercialInvoice.objects.all()
    serializer_class = CommercialInvoiceSerializer

class CommercialInvoiceDetail(RetrieveAPIView):
    """View para retrive un CommercialInvoice"""
    queryset = CommercialInvoice.objects.all()
    serializer_class = CommercialInvoiceSerializer

class CommercialInvoiceList(ListAPIView):
    """View para retrive todos los CommercialInvoices"""
    queryset = CommercialInvoice.objects.all()
    serializer_class = CommercialInvoiceSerializer

class CommercialInvoiceUpdate(UpdateAPIView):
    """View para update un CommercialInvoice"""
    queryset = CommercialInvoice.objects.all()
    serializer_class = UpdateCommercialInvoiceSerializer

class CommercialInvoiceDelete(DestroyAPIView):
    """View para delete un CommercialInvoice"""
    queryset = CommercialInvoice.objects.all()
    serializer_class = DeleteCommercialInvoiceSerializer


#                                               QUERY
