# Modelos para los Transformadores de Energia.
from .models import (
    Contract,
    Invoice
)
from energytransfers.serializers import CounterSerializer
# Serializer
from rest_framework import serializers


# =========================== Serializador para el Modulo Contract ==========================

# -----------------------------------------Contract------------------------------------------------


#get contrat with nested counter (that counter contains nested histories)
class ContractSerializer(serializers.ModelSerializer):
    counter = CounterSerializer()
    class Meta:
        model = Contract
        fields = [
            'contractNumber',
            'client',
            'counter',
            ]


# -----------------------------------------Invoice------------------------------------------------

#                                              CRUD
class CreateInvoiceSerializer(serializers.ModelSerializer):
    """Invoice para las operaciones Create"""
    #history = CreateHistorySerializer()
    class Meta:
        model = Invoice
        fields = [
            'consumptiondaysInvoice',
            'paymentdeadlineInvoice',
            'billingdateInvoice',
            'stateInvoice',
            'referencecodeInvoice',
            'total',
            'contract',
            ]

    def create(self, validated_data):
        #history = validated_data.pop('history')
        #custom = History.objects.create(**history)

        invoice = Invoice.objects.create(
            **validated_data
        )
        
        invoice.save()
        return invoice

class InvoiceSerializer(serializers.ModelSerializer):
    """Invoice para las operaciones Retrive"""
    
    #history = HistorySerializer()
    
    class Meta:
        model = Invoice
        fields = [
            'codeInvoice',
            'consumptiondaysInvoice',
            'paymentdeadlineInvoice',
            'billingdateInvoice',
            'stateInvoice',
            'referencecodeInvoice',
            'total',
            'contract',
            ]

class UpdateInvoiceSerializer(serializers.ModelSerializer):
    """Invoice para las operaciones Update"""
    class Meta:
        model = Invoice
        fields = [
            'consumptiondaysInvoice',
            'paymentdeadlineInvoice',
            'billingdateInvoice',
            'stateInvoice',
            'referencecodeInvoice',
            ]

    def update(self, instance, validated_data):
        invoice = super().update(instance, validated_data)
        return invoice

class DeleteInvoiceSerializer(serializers.ModelSerializer):
    """Invoice para las operaciones Delete"""
    class Meta:
        model = Invoice
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()

class InactivateInvoiceSerializer(serializers.ModelSerializer):
    """Invoice para las operaciones Inactive"""
    class Meta:
        model = Invoice
        fields = ['stateInvoice']

    def patch(self, request, *args, **kwargs):
        invoice = self.partial_update(request, *args, **kwargs)
        return invoice

#                                      Query
