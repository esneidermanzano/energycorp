# Modelos para los Transformadores de Energia.
from .models import (
    Payment,
    BanckPayment,
    DirectPayment
)
from datetime import date
from contract.models import (Invoice, Contract)
from contract.serializers import InvoiceSerializer
from energytransfers.models import Counter


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
class PaymenByContractSerializer(serializers.ModelSerializer):
    """Vista para ver los pagos hechos po un worker especifico pagos directos"""
    
    facturaPayment = InvoiceSerializer()
    class Meta:
        model = Payment
        fields = ['codePayment',
                  'valuePayment',
                  'datePayment',
                  'facturaPayment']

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
        #traigo la factura asociada a ese pago:
        numberInvocie =payment['facturaPayment']
        invoice = Invoice.objects.get(codeInvoice=numberInvocie.codeInvoice)  
        #caluclo la mora
        mora = ((date.today() - invoice.deadDatePay ).days / 100)
        print(mora)
        #validaciones pendejas para no pasar el 30%
        if (mora > 0.30):
            mora = 0.30
        if (mora < 0.0):
            mora = 0.0
        #Traigo el codigo de contrato asociada a esa factura:
        codeContract = invoice.contract.contractNumber
        #Traigo el contrato asociado a ese codigo
        contract = Contract.objects.get(contractNumber=codeContract)
        #Inyecto el valor de mora al contrato correspondiente.
        contract.interes_mora = mora
        contract.save()   
        #Desactiva la factura cuando crea el pago
        invoice.stateInvoice = True
        invoice.is_active = False
        invoice.save()
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
class BanckPaymenByBanckSerializer(serializers.ModelSerializer):
    """Vista para ver los pagos hechos po un worker especifico pagos directos"""
    class Meta:
        model = DirectPayment
        fields = '__all__'

    def get_queryset(self):
        pay = BanckPayment.objects.all().filter(
                banckPayment=self.kwargs['banckPayment']
        )
        return pay
    

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
        mora = ((date.today() - invoice.deadDatePay ).days / 100)
        #validaciones pendejas para no pasar el 30%
        if (mora > 0.30):
            mora = 0.30
        if (mora < 0.0):
            mora = 0.0
        #Traigo el codigo de contrato asociada a esa factura:
        codeContract = invoice.contract.contractNumber
        #Traigo el contrato asociado a ese codigo
        contract = Contract.objects.get(contractNumber=codeContract)
        #Inyecto el valor de mora al contrato correspondiente.
        contract.interes_mora = mora
        contract.save()   
        #Asemos la creación del pago y se asocia a el pago directo.
        paymentObj = Payment.objects.create(**payment)
        directPayment = DirectPayment.objects.create(
            payment=paymentObj, **validated_data)
        #Desactiva la factura cuando crea el pago
        invoice.stateInvoice = True
        invoice.is_active = False
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

class ReactivateDirectPaymentSerializer(serializers.ModelSerializer):
    """Pago para reactivar una factura"""

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
        value = payment['valuePayment'] 
        invoice = Invoice.objects.get(codeInvoice=numberInvocie.codeInvoice)
        #Traigo el codigo de contrato asociada a esa factura:
        codeContract = invoice.contract.contractNumber
        #Traigo el contrato asociado a ese codigo
        contract = Contract.objects.get(contractNumber=codeContract)
        #Traigo el id del contador a activar
        counterID = contract.counter.codeCounter
        #Traigo el contador asociado a ese codigo
        counter = Counter.objects.get(codeCounter=counterID)    
        #Validamos que pague la reconexion
        if (value != (invoice.total + 35000)):
            payment['valuePayment'] = (value + 35000)
        if ((invoice.is_active)and
              (counter.is_active == False)):
            """Si el valor que entroduje en el pago es igual a el de la factura 
            + los 35000 de reconexion y es la ultima factura realiza el proceso"""
            #Activo el contador
            counter.is_active = True
            counter.save()
            #Desactiva la factura cuando crea el pago
            invoice.is_active = False
            invoice.stateInovoice = True
            invoice.save()
        #Asemos la creación del pago y se asocia a el pago directo.
        paymentObj = Payment.objects.create(**payment)
        directPayment = DirectPayment.objects.create(
            payment=paymentObj, **validated_data)
        return directPayment


class DirectPaymenByWorkerSerializer(serializers.ModelSerializer):
    """Vista para ver los pagos hechos po un worker especifico pagos directos"""
    class Meta:
        model = DirectPayment
        fields = '__all__'

    def get_queryset(self):
        pay = DirectPayment.objects.all().filter(
            workerPayment=self.kwargs['workerPayment']
        )
        return pay
    