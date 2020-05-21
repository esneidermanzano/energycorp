from rest_framework import serializers
from users.models import (
    CustomUser,
    Client,
    Worker
    )
from energytransfers.models import Counter
from contract.models import Contract
from users.serializers import UserSerializer, ClientSerializer 
from energytransfers.serializers import CounterSerializer

class getNameUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'name', 
        ]


class MoraSerializer(serializers.ModelSerializer):
    
    user = getNameUserSerializer()
    class Meta:
        model = Client
        fields = [
            'id',    
            'user',
        ]
class ReportsCounterSerializer(serializers.ModelSerializer):
    """Counter para las operaciones Retrive"""    
    class Meta:
        model = Counter
        fields = [
            'codeCounter',
            'is_active'
            ]
class ServiceSuspendedSerializer(serializers.ModelSerializer):
    
    
    client = MoraSerializer()
    counter = ReportsCounterSerializer()
    class Meta:
        model = Contract
        fields = [
          #  'contractNumber',
            'client',
            'counter'          
            ]
class TopFiveCounterSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Counter
        fields = [
            'codeCounter',
            'latitudeCounter',
            'lengthCounter',
            'value',
            'addressCounter',
            'stratum',
            'transformatorCounter'
        ]

    """def get_historys(self, counter):
        qs = counter.historys.all().filter(
            counter=counter).order_by('-codeHistory')[:6]
        historys = HistorySerializer(qs, many=True, read_only=True).data
        return historys"""