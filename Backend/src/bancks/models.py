from django.db import models

# Create your models here.
""" The models in this File are the objetcs than respresent the pago,
    pago directo, pago banco."""


class Banck(models.Model):
    """Modelo para representar el objero Pago"""
    codeBanck = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )
    nameBanck = models.CharField(max_length=255)
    referenceBanck = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    