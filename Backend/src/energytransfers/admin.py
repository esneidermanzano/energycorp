# Django
from django.contrib import admin
# Models
from energytransfers.models import Substation, Transformator

# Register yours models here.
@admin.register(Substation)
class SubstationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'latitude', 'length', 'is_active')
    list_editable = ('latitude', 'length', 'is_active')
    search_fields = ('substation__latitude',
                     'substation__length')


@admin.register(Transformator)
class TransformatorAdmin(admin.ModelAdmin):
      list_display = ('pk', 'latitude', 'length', 'substation', 'is_active')
      list_editable = ('latitude', 'length', 'substation', 'is_active')
      search_fields = ('transformator__latitude',
                       'transformator__length')
