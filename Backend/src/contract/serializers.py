# Modelos para los Transformadores de Energia.
from .models import (
    InvoiceServices
)

# Serializer
from rest_framework import serializers


# =========================== Serializador para el Modulo Factures ==========================

# -----------------------------------------InvoiceServices------------------------------------------------

#                                              CRUD
class CreateInvoiceServicesSerializer(serializers.ModelSerializer):
    """InvoiceServices para las operaciones Create"""
    #history = CreateHistorySerializer()
    class Meta:
        model = InvoiceServices
        fields = [
            'consumptiondaysInvoice',
            'paymentdeadlineInvoice',
            'billingdateInvoice',
            'stateInvoice',
            'referencecodeInvoice',
            'total',
            'client',
            ]

    def create(self, validated_data):
        #history = validated_data.pop('history')
        #custom = History.objects.create(**history)

        invoiceServices = InvoiceServices.objects.create(
            **validated_data
        )
        
        invoiceServices.save()
        return invoiceServices

class InvoiceServicesSerializer(serializers.ModelSerializer):
    """InvoiceServices para las operaciones Retrive"""
    
    #history = HistorySerializer()
    
    class Meta:
        model = InvoiceServices
        fields = [
            'codeInvoice',
            'consumptiondaysInvoice',
            'paymentdeadlineInvoice',
            'billingdateInvoice',
            'stateInvoice',
            'referencecodeInvoice',
            'total',
            'client',
            ]

class UpdateInvoiceServicesSerializer(serializers.ModelSerializer):
    """InvoiceServices para las operaciones Update"""
    class Meta:
        model = InvoiceServices
        fields = [
            'consumptiondaysInvoice',
            'paymentdeadlineInvoice',
            'billingdateInvoice',
            'stateInvoice',
            'referencecodeInvoice',
            ]

    def update(self, instance, validated_data):
        invoiceServices = super().update(instance, validated_data)
        return invoiceServices

class DeleteInvoiceServicesSerializer(serializers.ModelSerializer):
    """InvoiceServices para las operaciones Delete"""
    class Meta:
        model = InvoiceServices
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()

class InactivateInvoiceServicesSerializer(serializers.ModelSerializer):
    """InvoiceServices para las operaciones Inactive"""
    class Meta:
        model = InvoiceServices
        fields = ['stateInvoice']

    def patch(self, request, *args, **kwargs):
        InvoiceServices = self.partial_update(request, *args, **kwargs)
        return InvoiceServices

#                                      Query
