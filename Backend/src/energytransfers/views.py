from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from energytransfers.models import (
    Substation,
    Transformator,
    Counter,
    History
    )

from energytransfers.serializers import (
    # CRUD SERIALIZERS
    SubstationSerializer,
    UpdateSubstationSerializer,
    CreateSubstationSerializer,
    InactivateSubstationSerializer,
    DeleteSubstationSerializer,

    TransformatorSerializer,
    CreateTransformatorSerializer,
    UpdateTransformatorSerializer,
    InactivateTransformatorSerializer,
    DeleteTransformatorSerializer,

    CounterSerializer,
    CreateCounterSerializer,
    UpdateCounterSerializer,
    InactivateCounterSerializer,
    DeleteCounterSerializer,

    HistorySerializer,
    UpdateHistorySerializer,
    CreateHistorySerializer,
    DeleteHistorySerializer
    # QUERY SERIALIZERS
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


class SubstationCreate(ListCreateAPIView):
    """View para crear una Subestacion"""
    queryset = Substation.objects.all()
    serializer_class = CreateSubstationSerializer

class SubstationDetail(RetrieveAPIView):
    """View para retrive una Subestacion""" 
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer

class SubstationList(ListAPIView):
    """View para retrive todas las Subestaciones"""
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer

class SubstationUpdate(UpdateAPIView):
    """View para update una Subestacion"""
    queryset = Substation.objects.all()
    serializer_class = UpdateSubstationSerializer

class SubstationDelete(DestroyAPIView):
    """View para delete una Subestacion"""
    queryset = Substation.objects.all()
    serializer_class = DeleteSubstationSerializer

class SubstationInactivate(UpdateAPIView):
    """View para delete una Subestacion"""
    queryset = Substation.objects.all()
    serializer_class = InactivateSubstationSerializer

#                                                   QUERY

#------------------------------------------------Transformator-------------------------------------

#                                                   CRUD

class TransformatorCreate(ListCreateAPIView):
    """View para delete un Transformator"""
    queryset = Transformator.objects.all()
    serializer_class = TransformatorSerializer

class TransformatorDetail(RetrieveAPIView):
    """View para retrive un Transformator"""
    queryset = Transformator.objects.all()
    serializer_class = TransformatorSerializer

class TransformatorList(ListAPIView):
    """View para retrive todos los Transformators"""
    queryset = Transformator.objects.all()
    serializer_class = TransformatorSerializer

class TransformatorUpdate(UpdateAPIView):
    """View para update un Transformator"""
    queryset = Transformator.objects.all()
    serializer_class = UpdateTransformatorSerializer

class TransformatorDelete(DestroyAPIView):
    """View para delete un Transformator"""
    queryset = Transformator.objects.all()
    serializer_class = DeleteTransformatorSerializer

class TransformatorInactivate(UpdateAPIView):
    """View para inactivate un Transformator"""
    queryset = Transformator.objects.all()
    serializer_class = InactivateTransformatorSerializer

#                                               QUERY

#----------------------------------------------Counter------------------------------------------------

#                                               CRUD

class CounterCreate(ListCreateAPIView):
    """View para delete un Counter"""
    queryset = Counter.objects.all()
    serializer_class = CreateCounterSerializer

class CounterDetail(RetrieveAPIView):
    """View para retrive un Counter"""
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer

class CounterList(ListAPIView):
    """View para retrive todos los Counter"""
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer

class CounterUpdate(UpdateAPIView):
    """View para update un Counter"""
    queryset = Counter.objects.all()
    serializer_class = UpdateCounterSerializer

class CounterDelete(DestroyAPIView):
    """View para delete un Counter"""
    queryset = Counter.objects.all()
    serializer_class = DeleteCounterSerializer

class CounterInactivate(UpdateAPIView):
    """View para inactivate un Counter"""
    queryset = Counter.objects.all()
    serializer_class = InactivateCounterSerializer


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