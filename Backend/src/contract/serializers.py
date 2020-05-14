# Modelos para los Transformadores de Energia.
from .models import (
    Contract,
    Invoice
)

# Serializer
from rest_framework import serializers


# =========================== Serializador para el Modulo Contract ==========================

# -----------------------------------------Contract------------------------------------------------

class ContractSerializer(serializers.ModelSerializer):
    
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
            'client',
            ]

    def create(self, validated_data):
        #history = validated_data.pop('history')
        #custom = History.objects.create(**history)

        Invoice = Invoice.objects.create(
            **validated_data
        )
        
        Invoice.save()
        return Invoice

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
            'client',
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
        Invoice = super().update(instance, validated_data)
        return Invoice

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
        Invoice = self.partial_update(request, *args, **kwargs)
        return Invoice

#                                      Query
