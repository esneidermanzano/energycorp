from django.db import models

from contract.models import Invoice
from bancks.models import Banck
from users.models import Worker

# Create your models here.
""" The models in this File are the objetcs than respresent the pago,
    pago directo, pago banco."""


class Payment(models.Model):
    """Modelo para representar el objero Pago"""
    codePayment = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )
    valuePayment = models.PositiveIntegerField()
    datePayment = models.DateTimeField(auto_now_add=True)
    facturaPayment = models.OneToOneField(Invoice,
                                          on_delete=models.CASCADE)


class DirectPayment(models.Model):
    """Modelo para representar el objero Pago"""
    codeDirectPayment = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )
    payment = models.OneToOneField(
        Payment, on_delete=models.CASCADE)
    workerPayment = models.ForeignKey(
        Worker,
        related_name='payments',
        on_delete=models.CASCADE
        )

class BanckPayment(models.Model):
    """Modelo para representar el objero Pago"""
    codeBanckPayment = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )
    payment = models.OneToOneField(
        Payment, on_delete=models.CASCADE)
    banckPayment = models.ForeignKey(
        Banck, 
        related_name='payments',
        on_delete=models.CASCADE
        )
