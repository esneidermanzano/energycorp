# Modelos para los Transformadores de Energia.
from .models import (
    Commercial,
    CommercialInvoice
)
# Serializer
from rest_framework import serializers

# =========================== Serializador para el Modulo Publicidad==================================

# -------------------------------------------Subestaciones-------------------------------------------

#                                               CRUD


class CreateCommercialSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Create"""
    class Meta:
        model = Commercial
        fields = [
            'urlCommercial',
            'nameCommercial',
            'contractorCommercial',
            'resourceCommercial',
            'is_active'
        ]

    def create(self, validated_data):
        commercial = Commercial.objects.create(
            urlCommercial=validated_data['urlCommercial'],
            nameCommercial=validated_data['nameCommercial'],
            contractorCommercial=validated_data['contractorCommercial'],
            resourceCommercial=validated_data['resourceCommercial'],
            is_active=validated_data['is_active']
        )
        commercial.save()
        return commercial


class CommercialSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Retrive"""
    class Meta:
        model = Commercial
        fields = '__all__'


class UpdateCommercialSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Update"""
    class Meta:
        model = Commercial
        fields = [
            'urlCommercial',
            'nameCommercial',
            'contractorCommercial',
            'resourceCommercial'
        ]

    def update(self, instance, validated_data):
        commercial = super().update(instance, validated_data)
        return commercial


class DeleteCommercialSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Delete"""
    class Meta:
        model = Commercial
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


class InactivateCommercialSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Inactivate"""
    class Meta:
        model = Commercial
        fields = [
            'is_active'
        ]

    def patch(self, request, *args, **kwargs):
        commercial = self.partial_update(request, *args, **kwargs)
        return commercial


#                                            Querys

# -----------------------------------------CommercialInvoice------------------------------------------------

#                                              CRUD
class CreateCommercialInvoiceSerializer(serializers.ModelSerializer):
    """CommercialInvoice para las operaciones Create"""
    class Meta:
        model = CommercialInvoice
        fields = [
            'invoiceservices',
            'commercial'
        ]

    def create(self, validated_data):
        commercialInvoice = CommercialInvoice.objects.create(
            invoiceservices=validated_data['invoiceservices'],
            commercial=validated_data['commercial']
        )
        commercialInvoice.save()
        return commercialInvoice


class CommercialInvoiceSerializer(serializers.ModelSerializer):
    """CommercialInvoice para las operaciones Retrive"""
    class Meta:
        model = CommercialInvoice
        fields = '__all__'


class UpdateCommercialInvoiceSerializer(serializers.ModelSerializer):
    """CommercialInvoice para las operaciones Update"""
    class Meta:
        model = CommercialInvoice
        fields = [
            'invoiceservices',
            'commercial'
        ]

    def update(self, instance, validated_data):
        commercialInvoice = super().update(instance, validated_data)
        return commercialInvoice


class DeleteCommercialInvoiceSerializer(serializers.ModelSerializer):
    """CommercialInvoice para las operaciones Delete"""
    class Meta:
        model = CommercialInvoice
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


#                                      Query
