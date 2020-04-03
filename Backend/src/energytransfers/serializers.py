from rest_framework import serializers
from energytransfers.models import Substation, Transformator

# importamos regular expressions
import re

# ========== Serializador para la substation ==========
class SubstationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Substation
        fields = ['latitude', 'length', 'is_active']

    
# ========== Serializador para crear la substation ==========
class CreateSubstationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Substation
        fields = ['latitude', 'length', 'is_active']

    def create(self, validated_data):
        substation = Substation.objects.create(
            latitude=validated_data['latitude'],
            length=validated_data['length'],
            is_active=validated_data['is_active']
        )
        substation.save()
        return substation


# ========== Serializador para actualizar la substation ==========
class UpdateSubstationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Substation
        fields = ['latitude', 'length', 'is_active']

    def update(self, instance, validated_data):
        print("===============IMPORMIENDO================")
        print(validated_data)
        substation = super().update(instance, validated_data)
        return substation

# ========== Serializador para inactivar la substation ==========


class InactivateSubstationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Substation
        fields = ['latitude', 'length', 'is_active']

    def patch(self, request, *args, **kwargs):
        Substation = self.partial_update(request, *args, **kwargs)
        return Substation
    


class DeleteSubstationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Substation
        fields = ['latitude', 'length', 'is_active', 'substation']

    def perform_destroy(self, instance):
            instance.delete()


    def inactivate(self, instance):
        print("===============IMPORMIENDO================")
        validated_data = instance
        if instance['is_active'] is True:
            valiated_data['is_active'] = False
        else:
            valiated_data['is_active'] = True
        print(validated_data)
        substation = super().update(instance, validated_data)
        return substation
 
# ========== Serializador para el Transformator ==========


class TransformatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transformator
        fields = ['latitude', 'length', 'is_active', 'substation']


# ========== Serializador para crear el transformator ==========
class CreateTransformatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transformator
        fields = ['latitude', 'length', 'is_active', 'substation']

    def create(self, validated_data):
        transformator = Transformator.objects.create(
            latitude=validated_data['latitude'],
            length=validated_data['length'],
            is_active=validated_data['is_active'],
            substation=validated_data['substation']
        )
        transformator.save()
        return transformator


# ========== Serializador para actualizar el transformator ==========
class UpdateTransformatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transformator
        fields = ['latitude', 'length', 'is_active', 'substation']

    def update(self, instance, validated_data):
        print("===============IMPORMIENDO================")
        print(validated_data)
        transformator = super().update(instance, validated_data)
        return transformator

# ========== Serializador para inactivar la Transformator ==========


class InactivateTransformatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transformator
        fields = ['latitude', 'length', 'is_active']

    def patch(self, request, *args, **kwargs):
        transformator = self.partial_update(request, *args, **kwargs)
        return transformator
    
    
 # ========== Serializador para actualizar el transformator ==========


class DeleteTransformatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transformator
        fields = ['latitude', 'length', 'is_active', 'substation']

    def perform_destroy(self, instance):
            instance.delete()
    def inactivate(self, instance):
        print("===============IMPORMIENDO================")
        validated_data = instance
        if instance['is_active'] is True:
            valiated_data['is_active'] = False
        else:
            valiated_data['is_active'] = True
        print(validated_data)
        Transformator = super().update(instance, validated_data)
        return Transformator
 
