#============ needed Imports to generate pdf file ===========
import datetime
import tempfile
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import render_to_string
from weasyprint import HTML
#============ end ===========
#==========needed Imports to send email================
from django.template.loader import get_template 
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import json
#============end=============

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import (
    Contract,
    Invoice
    )


from .serializers import (
    # CRUD SERIALIZERS
    ContractSerializer,

    InvoiceSerializer,
    CreateInvoiceSerializer,
    UpdateInvoiceSerializer,
    InactivateInvoiceSerializer,
    DeleteInvoiceSerializer
    # QUERY SERIALIZERS
)


from .permissions import (
    AllowAdmin,
    AllowManager,
    AllowOperator
)

from rest_framework.views import APIView
from rest_framework.response import Response

# ============================================Views para el modúlo de Contrato ==========================

#------------------------------------------------Contract-------------------------------------

class ContractList(ListAPIView):
    """View para retrive todos los Contratos"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class CreateContract(ListCreateAPIView):
    """View para retrive todos los Contratos"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
#------------------------------------------------Invoice-------------------------------------

#                                                   CRUD

class InvoiceCreate(ListCreateAPIView):
    """View para delete un Invoice"""
    queryset = Invoice.objects.all()
    serializer_class = CreateInvoiceSerializer

class InvoiceDetail(RetrieveAPIView):
    """View para retrive un Invoice"""
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceList(ListAPIView):
    """View para retrive todos los Invoices"""
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceUpdate(UpdateAPIView):
    """View para update un Invoice"""
    queryset = Invoice.objects.all()
    serializer_class = UpdateInvoiceSerializer

class InvoiceDelete(DestroyAPIView):
    """View para delete un Invoice"""
    queryset = Invoice.objects.all()
    serializer_class = DeleteInvoiceSerializer

class InvoiceInactivate(UpdateAPIView):
    """View para inactivate un Invoice"""
    queryset = Invoice.objects.all()
    serializer_class = InactivateInvoiceSerializer

#                                               QUERY

#--------------------------------------Generate PDF invoice---------------------------------                                      

data = {
        "contractNumber": 20200515,
        "invoice": [
            {
                "codeInvoice": 1,
                "consumptiondaysInvoice": 30,
                "paymentdeadlineInvoice": "2020-05-05",
                "billingdateInvoice": "2020-04-30",
                "stateInvoice": True,
                "referencecodeInvoice": "20200430(175915326153)3640602",
                "total": 242415.0,
                "contract": 20200515
            }
        ],
        "client": {
            "id": 1,
            "type_client": 1,
            "interes_mora": 0.0,
            "cycle": "1",
            "financial_state": "libre",
            "billing": "no se",
            "user": {
                "id": 1,
                "id_user": "1045127441",
                "name": "Cecilia Urquijo Barma",
                "email": "Cecilia@hotmail.com",
                "password": "pbkdf2_sha256$180000$JT8e0Cd32oKW$7Zei9Q+gAB7fEK+6iJRYdHxZnCoaCJKvCsXHBxEACqY=",
                "phone": "4982762",
                "address": "Diagonal 50B # 94 - 134",
                "neighborhood": "El bronx",
                "stratus": 4,
                "is_active": True,
                "is_staff": False,
                "is_superuser": False
            },
            "counters": [
                {
                    "codeCounter": 1,
                    "latitudeCounter": "3.429708",
                    "lengthCounter": "-76.501172",
                    "value": 227.0,
                    "addressCounter": "Cra. 28c #50-2 a 50-178",
                    "transformatorCounter": 1,
                    "historys": [
                        {
                            "codeHistory": 1,
                            "consumption": 17,
                            "registryHistory": "2020-04-30",
                            "counter": 1
                        },
                        {
                            "codeHistory": 2,
                            "consumption": 48,
                            "registryHistory": "2020-05-13",
                            "counter": 1
                        }
                    ]
                }
            ]
        }
    }

class GeneratePdf(View):
    def get(self, request, contract):
        """Generate pdf."""
        contractNumber = contract
        
        # Model data
        queryset = Contract.objects.filter(
            contractNumber__iexact=contractNumber)
        serializer_class = ContractSerializer(queryset, many=True).data

        if (queryset.exists()):
            nel = "save"
            # print(serializer_class)
        else:
            print("no existe")
        # Rendered
        print(serializer_class.values().contractNumber)
        print("================================================")
        print(serializer_class[0]['invoice'][0]['consumptiondaysInvoice'])

        html_string = render_to_string('contract/index.html', data)
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        result = html.write_pdf()

        # Creating http response
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=list_people.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())

        return response


#=============================View send invoice=======================================
class SendEmail(APIView):
  def post(self,request):      
      contractNumber = request.data.get('contractNumber')
      #Query for extract JOIN Invoice,Client, Contract, Counter, History with <pk> 
      #Example: {"contractNumber": 20200515}
      queryset = Contract.objects.filter(
          contractNumber__iexact=contractNumber)
      serializer_class = ContractSerializer(queryset, many=True).data

      if (queryset.exists()):
          #DICT->JSON       
          print(serializer_class)
          
          query= json.dumps(serializer_class)
          jsonQuery= json.loads(query)
          
          
          print(jsonQuery) 


          """fecha= datetime.date.today().month
          message_email= "Apreciado "\
               + client['name']+" generamos tu factura del mes " \
                 + str(fecha) + " con fecha limite de pago..."

          email= EmailMultiAlternatives(
               'Tu factura del mes',        #Title
                message_email,               #Message
                settings.EMAIL_HOST_USER,    #Email-corp
                [client['email']]            #Email-client
          )
      
          data = {
               'today': datetime.date.today(), 
               'amount': 39.99,
               'customer_name': 'Cooper Mann',
               'order_id': 1233434,
           }
           # Rendered pdf
          html_string = render_to_string('contract/index.html', data)
          html = HTML(string=html_string, base_url=request.build_absolute_uri())
          result = html.write_pdf()

          email.attach( client['name']+'.pdf',result, 'application/pdf')
          email.send()"""
          return Response({"message": jsonQuery})
      else:
           message = "El id proporcionado no existe o el usuario no está activo"
           return Response({"message": message , "code": 204, 'data': {}} )











































































































