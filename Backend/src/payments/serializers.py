# Modelos para los Transformadores de Energia.
from .models import (
    Payment,
    BanckPayment,
    DirectPayment
)
# Serializer
from rest_framework import serializers


# =========================== Serializador para el Modulo Payments =====================================

# -------------------------------------------Payments-----------------------------------------------------

#                                               CRUD

class CreatePaymentSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Create"""
    class Meta:
        model = Payment
        fields = [
            'valuePayment',
            'facturaPayment'
        ]

    def create(self, validated_data):
        payment = Payment.objects.create(
            valuePayment=validated_data['valuePayment'],
            facturaPayment=validated_data['facturaPayment']
        )
        payment.save()
        return payment


class PaymentSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Retrive"""
    class Meta:
        model = Payment
        fields = '__all__'


class UpdatePaymentSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Update"""
    class Meta:
        model = Payment
        fields = [
            'valuePayment',
            'facturaPayment'
        ]

    def update(self, instance, validated_data):
        payment = super().update(instance, validated_data)
        return payment


class DeletePaymentSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Delete"""
    class Meta:
        model = Payment
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


#                                            Querys

# -----------------------------------------BanckPayment------------------------------------------------

#                                              CRUD
class CreateBanckPaymentSerializer(serializers.ModelSerializer):
    """BanckPayment para las operaciones Create"""

    payment = PaymentSerializer()

    class Meta:
        model = BanckPayment
        fields = [
            'payment',
            'banckPayment'
        ]

    def create(self, validated_data):
        payment = validated_data.pop('payment')
        paymentObj = Payment.objects.create(**payment)
        banckPayment = BanckPayment.objects.create(
            payment=paymentObj, **validated_data)
        return banckPayment


class BanckPaymentSerializer(serializers.ModelSerializer):
    """BanckPayment para las operaciones Retrive"""
    class Meta:
        model = BanckPayment
        fields = '__all__'


class UpdateBanckPaymentSerializer(serializers.ModelSerializer):
    """BanckPayment para las operaciones Update"""
    class Meta:
        model = BanckPayment
        fields = [
            'payment',
            'banckPayment'
        ]

    def update(self, instance, validated_data):
        banckPayment = super().update(instance, validated_data)
        return banckPayment


class DeleteBanckPaymentSerializer(serializers.ModelSerializer):
    """BanckPayment para las operaciones Delete"""
    class Meta:
        model = BanckPayment
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()

#                                      Query

# -----------------------------------------DirectPayment------------------------------------------------

#                                              CRUD


class CreateDirectPaymentSerializer(serializers.ModelSerializer):
    """DirectPayment para las operaciones Create"""
    
    payment = PaymentSerializer()
    
    class Meta:
        model = DirectPayment
        fields = [
            'payment',
            'workerPayment'
        ]

    def create(self, validated_data):
        payment = validated_data.pop('payment')
        paymentObj = Payment.objects.create(**payment)
        directPayment = DirectPayment.objects.create(
            payment=paymentObj, **validated_data)
        return directPayment


class DirectPaymentSerializer(serializers.ModelSerializer):
    """DirectPayment para las operaciones Retrive"""
    class Meta:
        model = DirectPayment
        fields = '__all__'


class UpdateDirectPaymentSerializer(serializers.ModelSerializer):
    """DirectPayment para las operaciones Update"""
    class Meta:
        model = DirectPayment
        fields = [
            'payment',
            'workerPayment'
        ]

    def update(self, instance, validated_data):
        directPayment = super().update(instance, validated_data)
        return directPayment


class DeleteDirectPaymentSerializer(serializers.ModelSerializer):
    """DirectPayment para las operaciones Delete"""
    class Meta:
        model = DirectPayment
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


#                                           Query
