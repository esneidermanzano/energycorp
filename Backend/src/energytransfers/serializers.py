from rest_framework import serializers

# Modelos para los Transformadores de Energia.
from energytransfers.models import (
    Substation,
    Transformator,
    Counter,
    History
)


# =========================== Serializador para el Modulo Energy Transfer ==========================

# -------------------------------------------Subestaciones-------------------------------------------

#                                               CRUD

class CreateSubstationSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Create"""
    class Meta:
        model = Substation
        fields = [
            'latitudeSubstation',
            'lengthSubstation',
            'is_active'
        ]

    def create(self, validated_data):
        substation = Substation.objects.create(
            latitudeSubstation=validated_data['latitudeSubstation'],
            lengthSubstation=validated_data['lengthSubstation'],
            is_active=validated_data['is_active']
        )
        substation.save()
        return substation


class SubstationSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Retrive"""
    class Meta:
        model = Substation
        fields = '__all__'

class UpdateSubstationSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Update"""
    class Meta:
        model = Substation
        fields = [
            'latitudeSubstation',
            'lengthSubstation'
        ]

    def update(self, instance, validated_data):
        substation = super().update(instance, validated_data)
        return substation

class DeleteSubstationSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Delete"""
    class Meta:
        model = Substation
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()

class InactivateSubstationSerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Inactivate"""
    class Meta:
        model = Substation
        fields = [
            'is_active'
        ]

    def patch(self, request, *args, **kwargs):
        substation = self.partial_update(request, *args, **kwargs)
        return substation
    

#                                            Querys

# -----------------------------------------Transformator------------------------------------------------

#                                              CRUD
class CreateTransformatorSerializer(serializers.ModelSerializer):
    """Transformator para las operaciones Create"""
    class Meta:
        model = Transformator
        fields = [
            'latitudeTransformator',
            'lengthTransformator',
            'is_active',
            'substationTransformator'
            ]

    def create(self, validated_data):
        transformator = Transformator.objects.create(
            latitudeTransformator=validated_data['latitudeTransformator'],
            lengthTransformator=validated_data['lengthTransformator'],
            is_active=validated_data['is_active'],
            substationTransformator=validated_data['substationTransformator']
        )
        
        transformator.save()
        return transformator

class TransformatorSerializer(serializers.ModelSerializer):
    """Transformator para las operaciones Retrive"""
    class Meta:
        model = Transformator
        fields = '__all__'

class UpdateTransformatorSerializer(serializers.ModelSerializer):
    """Transformator para las operaciones Update"""
    class Meta:
        model = Transformator
        fields = [
            'latitudeTransformator',
            'lengthTransformator',
            'substationTransformator'
            ]

    def update(self, instance, validated_data):
        transformator = super().update(instance, validated_data)
        return transformator

class DeleteTransformatorSerializer(serializers.ModelSerializer):
    """Transformator para las operaciones Delete"""
    class Meta:
        model = Transformator
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()

class InactivateTransformatorSerializer(serializers.ModelSerializer):
    """Transformator para las operaciones Inactive"""
    class Meta:
        model = Transformator
        fields = ['is_active']

    def patch(self, request, *args, **kwargs):
        transformator = self.partial_update(request, *args, **kwargs)
        return transformator

#                                      Query

# -----------------------------------------Counter------------------------------------------------

#                                              CRUD


class CounterSerializer(serializers.ModelSerializer):
    """Counter para las operaciones Retrive"""    
    class Meta:
        model = Counter
        fields = [
            'codeCounter',
            'latitudeCounter',
            'lengthCounter',
            'value',
            'addressCounter',
            'transformatorCounter',
            ]

class CreateCounterSerializer(serializers.ModelSerializer):
    """Counter para las operaciones Create"""
    class Meta:
        model = Counter
        fields = [
            'latitudeCounter',
            'lengthCounter',
            'value',
            'addressCounter',
            'is_active',
            'transformatorCounter',
            'clientCounter'
            ]

    def create(self, validated_data):
        counter = Counter.objects.create(
            latitudeCounter=validated_data['latitudeCounter'],
            lengthCounter=validated_data['lengthCounter'],
            is_active=validated_data['is_active'],
            value=validated_data['value'],
            addressCounter=validated_data['addressCounter'],
            transformatorCounter=validated_data['transformatorCounter'],
            clientCounter=validated_data['clientCounter']
        )
        
        counter.save()
        return counter

        
class UpdateCounterSerializer(serializers.ModelSerializer):
    """Counter para las operaciones Update"""
    class Meta:
        model = Counter
        fields = [
            'latitudeCounter',
            'lengthCounter',
            'value',
            'addressCounter',
            'transformatorCounter'
            ]

    def update(self, instance, validated_data):
        counter = super().update(instance, validated_data)
        return counter
    
class DeleteCounterSerializer(serializers.ModelSerializer):
    """Counter para las operaciones Delete"""
    class Meta:
        model = Counter
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()
        
class InactivateCounterSerializer(serializers.ModelSerializer):
    """Transformator para las operaciones Inactive"""
    class Meta:
        model = Counter
        fields = ['is_active']

    def patch(self, request, *args, **kwargs):
        counter = self.partial_update(request, *args, **kwargs)
        return counter
    
#                                           Query
   
# -------------------------------------------History-------------------------------------------

#                                               CRUD

class HistorySerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Retrive"""
    class Meta:
        model = History
        fields = '__all__'
 
class CreateHistorySerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Create"""
    class Meta:
        model = History
        fields = [
            'counter',
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

class UpdateHistorySerializer(serializers.ModelSerializer):
    """Serializador para las operaciones Update"""
    class Meta:
        model = History
        fields = [
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


#==================== obtener contador con historias les anidadas ==================
class CounterHistoriesSerializer(serializers.ModelSerializer):
    historys = serializers.SerializerMethodField()
    
    class Meta:
        model = Counter
        fields = [
            'codeCounter',
            'latitudeCounter',
            'lengthCounter',
            'value',
            'addressCounter',
            'transformatorCounter',
            'historys'
            ]

    def get_historys(self, counter):
        print("================================")
        print(counter)
        qs = counter.historys.all().filter(
            counter=counter).order_by('-codeHistory')[:2]
        historys = HistorySerializer(qs, many=True, read_only=True).data
        print(historys)
        return historys

    
    