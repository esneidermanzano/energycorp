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
    interes_mora = models.FloatField()
    client = models.ForeignKey(
        Client, related_name='client', on_delete=models.PROTECT)
    counter = models.OneToOneField(
        Counter, related_name='counter', on_delete=models.PROTECT, unique=True)


class Invoice(models.Model):
    """Modelo para reprsentar el objeto Recibo"""
    codeInvoice = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='invoicenumber'
    )
    billingDate = models.DateField(default=datetime.date.today)
    deadDatePay = models.DateField(default=datetime.datetime.now()+datetime.timedelta(days=10))
    counter =  models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    stratum = models.PositiveSmallIntegerField()
    currentRecord = models.PositiveIntegerField()
    pastRecord = models.PositiveIntegerField()
    basicTake = models.PositiveIntegerField()
    remainder = models.PositiveIntegerField()
    unitaryValue = models.PositiveIntegerField()
    interestMora = models.PositiveIntegerField(default=0)
    totalMora = models.FloatField(default=0)
    overdue = models.FloatField(default=0)
    intakes = models.CharField(max_length=40)
    referencecodeInvoice = models.CharField(max_length=30)
    total = models.FloatField(null=False)
    stateInvoice = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    contract = models.ForeignKey(
        Contract, related_name='invoice', on_delete=models.PROTECT)