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
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import (
    InvoiceServices
    )


from .serializers import (
    # CRUD SERIALIZERS

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

#------------------------------------------------InvoiceServices-------------------------------------

#                                                   CRUD

class InvoiceServicesCreate(ListCreateAPIView):
    """View para delete un InvoiceServices"""
    queryset = InvoiceServices.objects.all()
    serializer_class = CreateInvoiceServicesSerializer

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














































































































