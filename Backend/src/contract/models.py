from django.db import models
import datetime
from users.models import Client
from energytransfers.models import Counter

# Create your models here.
""" The models in this File are the objetcs than respresent the history,
    publicity, invoice services and counters."""

class Contract(models.Model):
    """Modelo para reprsentar el objeto contrato"""
    contractNumber = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )
    client = models.ForeignKey(
        Client, related_name='client', on_delete=models.PROTECT)
    counter = models.ForeignKey(
        Counter, related_name='counter', on_delete=models.PROTECT)


class Invoice(models.Model):
    """Modelo para reprsentar el objeto Recibo"""
    codeInvoice = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )
    consumptiondaysInvoice = models.PositiveIntegerField()
    paymentdeadlineInvoice = models.DateField()
    billingdateInvoice = models.DateField(default=datetime.date.today)
    stateInvoice = models.BooleanField(default=False)
    referencecodeInvoice = models.CharField(max_length=30)
    total = models.FloatField(null=False)
    contract = models.ForeignKey(
        Contract, related_name='contract', on_delete=models.PROTECT)

