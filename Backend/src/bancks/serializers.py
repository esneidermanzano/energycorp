# Modelos para los Transformadores de Energia.
from .models import Banck
# Serializer
from rest_framework import serializers

# =========================== Serializador para el Modulo Bancos ==========================

# -------------------------------------------Banck-------------------------------------------

#                                               CRUD

class CreateBanckSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Create"""
    class Meta:
        model = Banck
        fields = [
            'nameBanck',
            'referenceBanck',
            'is_active'
        ]

    def create(self, validated_data):
        banck = Banck.objects.create(
            nameBanck=validated_data['nameBanck'],
            referenceBanck=validated_data['referenceBanck'],
            is_active=validated_data['is_active']
        )
        banck.save()
        return banck


class BanckSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Retrive"""
    class Meta:
        model = Banck
        fields = '__all__'

class UpdateBanckSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Update"""
    class Meta:
        model = Banck
        fields = [
            'nameBanck',
            'referenceBanck'
        ]

    def update(self, instance, validated_data):
        banck = super().update(instance, validated_data)
        return banck

class DeleteBanckSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Delete"""
    class Meta:
        model = Banck
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()

class InactivateBanckSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Inactivate"""
    class Meta:
        model = Banck
        fields = [
            'is_active'
        ]

    def patch(self, request, *args, **kwargs):
        banck = self.partial_update(request, *args, **kwargs)
        return banck
    

#                                            Querys