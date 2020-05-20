# Modelos para los Transformadores de Energia.
from .models import (
    Payment,
    BanckPayment,
    DirectPayment
)
from datetime import date
from contract.models import (Invoice, Contract)
from users.models import (Client)


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
        paymentObj = Payment.objects.create(**payment,
                                            **validated_data)
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
        #capturo el diccionario de pago:
        payment = validated_data.pop('payment')
        #traigo la factura asociada a ese pago:
        numberInvocie =payment['facturaPayment']
        invoice = Invoice.objects.get(codeInvoice=numberInvocie.codeInvoice)  
        #caluclo la mora
        mora = ((date.today() - invoice.paymentdeadlineInvoice ).days / 100)
        print(mora)
        #validaciones pendejas para no pasar el 30%
        if (mora > 0.30):
            mora = 0.30
        if (mora < 0.0):
            mora = 0.0
        #Traigo el contrato asociada a esa factura:
        codeClient = invoice.contract.client.id
        #Traigo el Cliente asociado a ese contrato
        client = Client.objects.get(id=codeClient)
        #Inyecto el valor de mora al cliente correspondiente.
        client.interes_mora = mora
        client.save()   
        #Asemos la creación del pago y se asocia a el pago directo.
        paymentObj = Payment.objects.create(**payment)
        directPayment = DirectPayment.objects.create(
            payment=paymentObj, **validated_data)
        #Desactiva la factura cuando crea el pago
        invoice.stateInvoice = True
        invoice.save()
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
