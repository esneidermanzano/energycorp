from django.shortcuts import render
from rest_framework.views import View

from rest_framework.generics import ListAPIView 
from users.models import Client
from energytransfers.models import Counter,History
from contract.models import Contract
from rest_framework.response import Response

import json
from django.db.models import F

from django.http import HttpResponse

from .serializers import (
    MoraSerializer,
    ServiceSuspendedSerializer,
    UserSerializer
)
from contract.serializers import ContractSerializer
# Create your views here.

class MoraAndSuspended(View):
    def get(self, request):
        queryset1 =  Contract.objects.exclude(
            interes_mora__iexact=0.0).filter(
                client__user__is_active=True).annotate(
                        id=F( 'client__id'),
                        name= F('client__user__name')
                    
                ).values('id','interes_mora', 'name')
       
        queryset = Contract.objects.exclude(counter__is_active=True)
       
        query = ServiceSuspendedSerializer(
            queryset,many=True
        ).data
       
       
       
        dicc= []
        for i in range(len(query)):
            datos = {

                "id": "",
                "name":"",
                "codeCounter": "",
                "is_active":""
            }
            datos['id']= query[i]['client']['id']
            datos['name']= query[i]['client']['user']['name']
            datos['codeCounter']= query[i]['counter']['codeCounter']
            datos['is_active']= query[i]['counter']['is_active']
           
            dicc.append(datos)
        
        response={
            "mora":"",
            "suspended":""
        }
        response['mora']=list(queryset1)
        response['suspended']=dicc


        return HttpResponse(json.dumps(response))   
"""class TopFiveCounters(View):
     def get(self, request):
        queryset1 =  Client.objects.filter(interes_mora__iexact=0.0).filter(user__is_active=True)
        
   

        return HttpResponse(json.dumps(response))     """