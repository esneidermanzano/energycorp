from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import (
    Payment,
    BanckPayment,
    DirectPayment
    )

from .serializers import (
    
    # CRUD SERIALIZERS
    PaymentSerializer,
    UpdatePaymentSerializer,
    CreatePaymentSerializer,
    DeletePaymentSerializer,

    BanckPaymentSerializer,
    CreateBanckPaymentSerializer,
    UpdateBanckPaymentSerializer,
    DeleteBanckPaymentSerializer,

    DirectPaymentSerializer,
    CreateDirectPaymentSerializer,
    UpdateDirectPaymentSerializer,
    DeleteDirectPaymentSerializer,
    # QUERY SERIALIZERS
    ReactivateDirectPaymentSerializer,
    DirectPaymenByWorkerSerializer,
    BanckPaymenByBanckSerializer,
    PaymenByContractSerializer
)

from .permissions import (
    AllowAdmin,
    AllowManager,
    AllowOperator
)

from rest_framework.views import APIView
from rest_framework.response import Response

# ============================================Views para el modúlo Energy Transfers==========================

#----------------------------------------------------Subestaciones-------------------------------------                                      

#                                                       CRUD


class PaymentCreate(ListCreateAPIView):
    """View para crear una Subestacion"""
    queryset = Payment.objects.all()
    serializer_class = CreatePaymentSerializer

class PaymentDetail(RetrieveAPIView):
    """View para retrive una Subestacion""" 
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentList(ListAPIView):
    """View para retrive todas las Subestaciones"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentUpdate(UpdateAPIView):
    """View para update una Subestacion"""
    queryset = Payment.objects.all()
    serializer_class = UpdatePaymentSerializer

class PaymentDelete(DestroyAPIView):
    """View para delete una Subestacion"""
    queryset = Payment.objects.all()
    serializer_class = DeletePaymentSerializer


#                                                   QUERY
class PaymentByContractList(ListAPIView):
    """View para retrive todas las Subestaciones"""
    queryset = Payment.objects.all()
    serializer_class = PaymenByContractSerializer
    
    def get_queryset(self):
        pay = Payment.objects.all().filter(
        facturaPayment__contract=self.kwargs['contract']
        )
        return pay

#------------------------------------------------BanckPayment-------------------------------------

#                                                   CRUD

class BanckPaymentCreate(ListCreateAPIView):
    """View para delete un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = CreateBanckPaymentSerializer

class BanckPaymentDetail(RetrieveAPIView):
    """View para retrive un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = BanckPaymentSerializer

class BanckPaymentList(ListAPIView):
    """View para retrive todos los BanckPayments"""
    queryset = BanckPayment.objects.all()
    serializer_class = BanckPaymentSerializer

class BanckPaymentUpdate(UpdateAPIView):
    """View para update un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = UpdateBanckPaymentSerializer

class BanckPaymentDelete(DestroyAPIView):
    """View para delete un BanckPayment"""
    queryset = BanckPayment.objects.all()
    serializer_class = DeleteBanckPaymentSerializer


#                                               QUERY
class BanckPaymentByBanckList(ListAPIView):
    """View para retrive todos los BanckPayments"""
    queryset = BanckPayment.objects.all()
    serializer_class = BanckPaymenByBanckSerializer



#----------------------------------------------DirectPayment------------------------------------------------

#                                               CRUD

class DirectPaymentCreate(ListCreateAPIView):
    """View para delete un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = CreateDirectPaymentSerializer

class DirectPaymentDetail(RetrieveAPIView):
    """View para retrive un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = DirectPaymentSerializer

class DirectPaymentList(ListAPIView):
    """View para retrive todos los DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = DirectPaymentSerializer

class DirectPaymentUpdate(UpdateAPIView):
    """View para update un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = UpdateDirectPaymentSerializer

class DirectPaymentDelete(DestroyAPIView):
    """View para delete un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = DeleteDirectPaymentSerializer

#                           Query
class DirectPaymentReactivate(ListCreateAPIView):
    """View para delete un DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = ReactivateDirectPaymentSerializer
    

class DirectPaymenByWorker(ListAPIView):
    """View para retrive todos los DirectPayment"""
    queryset = DirectPayment.objects.all()
    serializer_class = DirectPaymenByWorkerSerializer
    
    