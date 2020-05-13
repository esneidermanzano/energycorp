# Modelos para los Transformadores de Energia.
from .models import (
    History,
    InvoiceServices
)

# Serializer
from rest_framework import serializers


# =========================== Serializador para el Modulo Factures ==========================

# -------------------------------------------History-------------------------------------------

#                                               CRUD

class CreateHistorySerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Create"""
    class Meta:
        model = History
        fields = [
            'counter'
            'consumption'
            #'registryHistory'
        ]

    def create(self, validated_data):
        history = History.objects.create(
            counter=validated_data['counter'],
            consumption=validated_data['consumption']
            #registryHistory=validated_data['registryHistory']
        )
        history.save()
        return history


class HistorySerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Retrive"""
    class Meta:
        model = History
        fields = '__all__'

class UpdateHistorySerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Update"""
    class Meta:
        model = History
        fields = [
            'registryHistory',
            'consumption'
        ]

    def update(self, instance, validated_data):
        history = super().update(instance, validated_data)
        return history

class DeleteHistorySerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Delete"""
    class Meta:
        model = History
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


#                                            Querys

# -----------------------------------------InvoiceServices------------------------------------------------

#                                              CRUD
class CreateInvoiceServicesSerializer(serializers.ModelSerializer):
    """InvoiceServices para las operaciones Create"""
    
    class Meta:
        model = InvoiceServices
        fields = [
            'consumptiondaysInvoice',
            'paymentdeadlineInvoice',
            'billingdateInvoice',
            'stateInvoice',
            'referencecodeInvoice',
            'history'
            ]

    def create(self, validated_data):
        invoiceServices = InvoiceServices.objects.create(
            consumptiondaysInvoice=validated_data['latitudeInvoiceServices'],
            paymentdeadlineInvoice=validated_data['lengthInvoiceServices'],
            billingdateInvoice=validated_data['is_active'],
            stateInvoice=validated_data['HistoryInvoiceServices'],
            referencecodeInvoice=validated_data['HistoryInvoiceServices'],
            history=validated_data['HistoryInvoiceServices']
        )
        
        invoiceServices.save()
        return invoiceServices

class InvoiceServicesSerializer(serializers.ModelSerializer):
    """InvoiceServices para las operaciones Retrive"""
    
    history = HistorySerializer()
    
    class Meta:
        model = InvoiceServices
        fields = [
            'codeInvoice',
            'consumptiondaysInvoice',
            'paymentdeadlineInvoice',
            'billingdateInvoice',
            'stateInvoice',
            'referencecodeInvoice',
            'history'
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
            'history'
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
