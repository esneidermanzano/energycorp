#============ needed Imports to generate pdf file ===========
import datetime
import tempfile
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import render_to_string
from weasyprint import HTML
#============ end ===========


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

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        """Generate pdf."""
        # Model data
        data = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        # Rendered
        html_string = render_to_string('factures/index.html', data)
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














































































































