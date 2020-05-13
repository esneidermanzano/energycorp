from django.db import models
import datetime
from users.models import Worker
from energytransfers.models import Counter

# Create your models here.
""" The models in this File are the objetcs than respresent the history,
    publicity, invoice services and counters."""


class History(models.Model):
    """Modelo para representar el objero history"""
    codeHistory = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
        )
    counter = models.ForeignKey(
        Counter, related_name='historys', on_delete=models.CASCADE)
    registryHistory = models.DateField(auto_now_add=True)
    


class InvoiceServices(models.Model):
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
    history = models.OneToOneField(History, on_delete=models.CASCADE)

