from django.db import models
import datetime
from users.models import Worker
from energytransfers.models import Counter

# Create your models here.
class History(models.Model):
    #id_history= models.AutoField(primary_key= True)
    counter= models.ForeignKey(Counter,on_delete=models.CASCADE)
    init_date= models.DateField()
    final_date=models.DateField()


class Publicity(models.Model):
    #code_publicity= models.AutoField(primary_key=True)
    contractor= models.CharField(max_length=30)
    category= models.CharField(max_length=15)
    url_resource= models.URLField(max_length=200)


class Bill(models.Model):
    #bill_number= models.AutoField(primay_key=True)
    consumption_days= models.PositiveIntegerField()
    payment_deadline= models.DateField()
    billing_date= models.DateField(default=datetime.date.today) 
    state= models.BooleanField(default=False)
    reference_code= models.CharField(max_length=30)
    history= models.OneToOneField(History, on_delete= models.CASCADE)
    publicity= models.ManyToManyField(Publicity)

"""class BillPublicity(models.Model):
    bill= models.ForeignKey(Bill)
















































    publicity= models.ForeignKey(Publicity)"""

class Bank(models.Model):
    #id_bank= models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)

class Payment(models.Model):
    #transaction_code= models.AutoField(primary_key= True)
    hour= models.TimeField(default=datetime.time)
    transaction_date= models.DateField(default= datetime.date.today)
    bill= models.OneToOneField(Bill,on_delete=models.CASCADE) 

class BankPayment(models.Model):
    transaction_code= models.OneToOneField(Payment,on_delete=models.CASCADE,primary_key=True)
    bank= models.ForeignKey(Bank, on_delete= models.CASCADE) 


class DirectPayment(models.Model):
    transaction_code= models.OneToOneField(Payment,on_delete=models.CASCADE,primary_key=True)
    worker= models.ForeignKey(Worker, on_delete= models.CASCADE)






