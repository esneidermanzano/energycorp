from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import (
    History,
    InvoiceServices
    )


from .serializers import (
    # CRUD SERIALIZERS
    HistorySerializer,
    UpdateHistorySerializer,
    CreateHistorySerializer,
    DeleteHistorySerializer,

    InvoiceServicesSerializer,
    CreateInvoiceServicesSerializer,
    UpdateInvoiceServicesSerializer,
    InactivateInvoiceServicesSerializer,
    DeleteInvoiceServicesSerializer
    # QUERY SERIALIZERS
)


from .permissions import (
    AllowAdmin,
    AllowManager,
    AllowOperator
)

from rest_framework.views import APIView
from rest_framework.response import Response

# ============================================Views para el modúlo de Facturas ==========================

#----------------------------------------------------Historys-------------------------------------                                      

#                                                       CRUD


class HistoryCreate(ListCreateAPIView):
    """View para crear una Subestacion"""
    queryset = History.objects.all()
    serializer_class = CreateHistorySerializer

class HistoryDetail(RetrieveAPIView):
    """View para retrive una Subestacion""" 
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryList(ListAPIView):
    """View para retrive todas las Subestaciones"""
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryUpdate(UpdateAPIView):
    """View para update una Subestacion"""
    queryset = History.objects.all()
    serializer_class = UpdateHistorySerializer

class HistoryDelete(DestroyAPIView):
    """View para delete una Subestacion"""
    queryset = History.objects.all()
    serializer_class = DeleteHistorySerializer


#                                                   QUERY

#------------------------------------------------InvoiceServices-------------------------------------

#                                                   CRUD

class InvoiceServicesCreate(ListCreateAPIView):
    """View para delete un InvoiceServices"""
    queryset = InvoiceServices.objects.all()
    serializer_class = InvoiceServicesSerializer

class InvoiceServicesDetail(RetrieveAPIView):
    """View para retrive un InvoiceServices"""
    queryset = InvoiceServices.objects.all()
    serializer_class = InvoiceServicesSerializer

class InvoiceServicesList(ListAPIView):
    """View para retrive todos los InvoiceServicess"""
    queryset = InvoiceServices.objects.all()
    serializer_class = InvoiceServicesSerializer

class InvoiceServicesUpdate(UpdateAPIView):
    """View para update un InvoiceServices"""
    queryset = InvoiceServices.objects.all()
    serializer_class = UpdateInvoiceServicesSerializer

class InvoiceServicesDelete(DestroyAPIView):
    """View para delete un InvoiceServices"""
    queryset = InvoiceServices.objects.all()
    serializer_class = DeleteInvoiceServicesSerializer

class InvoiceServicesInactivate(UpdateAPIView):
    """View para inactivate un InvoiceServices"""
    queryset = InvoiceServices.objects.all()
    serializer_class = InactivateInvoiceServicesSerializer

#                                               QUERY




















































































































