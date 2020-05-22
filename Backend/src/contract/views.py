#============ needed Imports to generate pdf file ===========
import tempfile
from .utils import getInvoiceData, generateHistoryAndInvoices
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
    CreateFullContractSerializer,
    ContractClienteInvoiceSerializer,
    SuperJoinSerializer,

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
    """View para crear contrato con cliente y contador existente"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class CreateFullContract(ListCreateAPIView):
    """View para crear contrato+user+counter"""
    queryset = Contract.objects.all()
    serializer_class = CreateFullContractSerializer

class GetFullContractJoin(ListCreateAPIView):
    """View para ver contrato con cliente y contador"""
    queryset = Contract.objects.all()
    serializer_class = SuperJoinSerializer
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

#Obtener las  ultimas 6 facturas dado un numero de contrato
class GetInvoiceByContract(APIView):
    def post(self,request):
        try:
            contractNumber = request.data.get('contractNumber')
            queryset = Invoice.objects.filter(
                contract=contractNumber).order_by('-codeInvoice')[:5]
            serializer = InvoiceSerializer(queryset, many=True).data
            if (queryset.exists()):
                return Response({ "error": False,"find": True, "invoices": serializer})
            else:
                message = "Numero de contrato erroneo"
                return Response({ "error": False, "find": False, "message": message} )
        except:
            message = "Error al buscar las facturas, intelo mas tarde"
            return Response({"error": True, "message": message} )



#obtener un afactura en formato pdf
class GeneratePdf(APIView):
    def get(self, request, contract, factura):
        generateHistoryAndInvoices()
        try:
            queryset = Contract.objects.filter(contractNumber__iexact=contract)
            datos = {}
            if (queryset.exists()):  
                try:              
                    query = ContractClienteInvoiceSerializer(
                        queryset, many=True, context={'codeInvoice': factura}
                    ).data[0]                
                    datos = getInvoiceData(query)
                    # Rendered
                    html_string = render_to_string('contract/index.html', datos)
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
                except Exception as e:
                    message = "Error al buscar la factura, confirme el numero"
                    return Response({"error": False, "find": False, "message": str(e)} )
            else:
                message = "Numero de contrato erroneo"
                return Response({ "error": False, "find": False, "message": message} )           
        except:
            message = "Error al buscar la factura, intelo mas tarde"
            return Response({"error": True, "message": message} )


#=============================View send invoice=======================================
class SendEmail(APIView):
  def get(self, request, contract, factura):
        generateHistoryAndInvoices()
        try:
            queryset = Contract.objects.filter(contractNumber__iexact=contract)
            datos = {}
            if (queryset.exists()):  
                try:              
                    query = ContractClienteInvoiceSerializer(
                        queryset, many=True, context={'codeInvoice': factura}
                    ).data[0]                
                    datos = getInvoiceData(query)
                    # Rendered
                    html_string = render_to_string('contract/index.html', datos)
                    html = HTML(string=html_string, base_url=request.build_absolute_uri())
                    result = html.write_pdf()

                    
                    message_email= "Apreciado "\
                       + datos['name']+" generamos tu factura del mes " \
                         + datos['payMonth'] + " con fecha limite de pago "+  datos['deadDatePay']


                    email= EmailMultiAlternatives(
                         'Tu factura del mes',        #Title
                          message_email,               #Message
                          settings.EMAIL_HOST_USER,    #Email-corp
                          [query['client']['user']['email']]            #Email-client
                    )
                    email.attach( datos['name']+'.pdf',result, 'application/pdf')
                    email.send()
                    message = "La factura fue enviada"

                    return Response({"error": False, "find": True, "message": message} )
                except Exception as e:
                    message = "Error al buscar la factura, confirme el numero"
                    return Response({"error": False, "find": False, "message": str(e)} )
            else:
                message = "Numero de contrato erroneo"
                return Response({ "error": False, "find": False, "message": message} )           
        except:
            message = "Error al buscar la factura, intelo mas tarde"
            return Response({"error": True, "message": message} )  
  
