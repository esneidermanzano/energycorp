# Modelos para los Transformadores de Energia.
from energytransfers.models import (
    Substation,
    Transformator,
    Counter
)
# Serializer
from rest_framework import serializers

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
            'is_activeSubstation'
        ]

    def create(self, validated_data):
        substation = Substation.objects.create(
            latitudeSubstation=validated_data['latitudeSubstation'],
            lengthSubstation=validated_data['lengthSubstation'],
            is_active=validated_data['is_activeSubstation']
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
class CreateCounterSerializer(serializers.ModelSerializer):
    """Counter para las operaciones Create"""
    class Meta:
        model = Counter
        fields = [
            'latitudeCounter',
            'lengthCounter',
            'counter',
            'addressCounter',
            'is_active',
            'transformatorCounter'
            ]

    def create(self, validated_data):
        counter = Transformator.objects.create(
            latitudeCounter=validated_data['latitudeCounter'],
            lengthCounter=validated_data['lengthCounter'],
            is_active=validated_data['is_active'],
            counter=validated_data['counter'],
            addressCounter=validated_data['addressCounter'],
            transformatorCounter=validated_data['transformatorCounter']
        )
        
        counter.save()
        return counter
    
class CounterSerializer(serializers.ModelSerializer):
    """Counter para las operaciones Retrive"""
    class Meta:
        model = Counter
        fields = '__all__'
        
class UpdateCounterSerializer(serializers.ModelSerializer):
    """Counter para las operaciones Update"""
    class Meta:
        model = Counter
        fields = [
            'latitudeCounter',
            'lengthCounter',
            'counter',
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
   