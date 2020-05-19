# Django
from django.contrib import admin
# Models
from energytransfers.models import (
    Substation,
    Transformator,
    Counter
)

# Register yours models here.
@admin.register(Substation)
class SubstationAdmin(admin.ModelAdmin):
    list_display = ('codeSubstation', 'latitudeSubstation',
                    'lengthSubstation', 'is_active')
    list_editable = ('latitudeSubstation', 'lengthSubstation', 'is_active')
    search_fields = ('substation__latitude',
                     'substation__length')


@admin.register(Transformator)
class TransformatorAdmin(admin.ModelAdmin):
    list_display = ('codeTransformator', 'latitudeTransformator',
                    'lengthTransformator', 'substationTransformator', 'is_active')
    list_editable = ('latitudeTransformator', 'lengthTransformator',
                     'substationTransformator', 'is_active')
    search_fields = ('transformator__latitudeTransformator',
                     'transformator__lengthTransformator')


@admin.register(Counter)
class TransformatorAdmin(admin.ModelAdmin):
    list_display = ('codeCounter', 'latitudeCounter',
                    'lengthCounter', 'transformatorCounter',
                    'addressCounter', 'counter', 'is_active')
    #list_editable = ('is_active')
    search_fields = ('counter__latitudeCounter',
                     'counter__lengthCounter')
