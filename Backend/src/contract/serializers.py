# Modelos para los Transformadores de Energia.
from .models import (
    Contract,
    Invoice
)
from energytransfers.serializers import (
    CounterHistoriesSerializer,
    CounterSerializer
)
from users.serializers import ClientSerializer
# Serializer
from rest_framework import serializers


# -----------------------------------------Invoice------------------------------------------------

#                                              CRUD
class CreateInvoiceSerializer(serializers.ModelSerializer):
    """Invoice para las operaciones Create"""
    #history = CreateHistorySerializer()
    class Meta:
        model = Invoice
        fields = '__all__'

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
        fields = '__all__'
 

class UpdateInvoiceSerializer(serializers.ModelSerializer):
    """Invoice para las operaciones Update"""
    class Meta:
        model = Invoice

        
        fields = [
            'stateInvoice',
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

# =========================== Serializador para el Modulo Contract ==========================

# -----------------------------------------Contract------------------------------------------------

class ContractSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contract
        fields = [
            'contractNumber',
            'interes_mora', 
            'client',
            'counter',
            ]

#create a contract, user, and counter at same time
class CreateFullContractSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    counter = CounterSerializer()

    class Meta:
        model = Contract
        fields = [
            'contractNumber',
            'interes_mora',
            'client',
            'counter',
            ]

#get a contract and client
class ContractClientSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    
    class Meta:
        model = Contract
        fields = [
            'contractNumber',
            'client',
            ]

#get one invoice to print pdf
class ContractClienteInvoiceSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    invoice = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = [
            'contractNumber',
            'client',
            'invoice',           
            ]

    def get_invoice(self, contract):
        print("==================================")
        codeInvoice= self.context.get('codeInvoice')
        qs = Invoice.objects.all().filter(
            codeInvoice=codeInvoice)
        invoice = InvoiceSerializer(qs, many=True, read_only=True).data[0]
        return invoice

#get contrat with nested invoice and client(that client contains nested counter(that counter contains nested histories)) 
class SuperJoinSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    counter = CounterHistoriesSerializer()
    invoice = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = [
            'contractNumber',
            'interes_mora',
            'client',
            'counter',
            'invoice',           
            ]

    def get_invoice(self, contract):
        qs = Invoice.objects.all().filter(
            contract=contract).order_by('-codeInvoice')[:5]
        invoice = InvoiceSerializer(qs, many=True, read_only=True).data
        return invoice

#                                      Query
