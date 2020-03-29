from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin, AbstractUser
import datetime
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        user = self.create_user(email, password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(email, password, **extra_fields)
        return user

class CustomUser(AbstractUser):

    username = None
    first_name = None
    last_name = None
    phone_validate = RegexValidator(regex=r'^\+?1?\d{7,10}$', message= "Numero incorrecto")

    id_user = models.CharField(validators = [phone_validate], max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True, null= True, unique= True)
    #password = models.CharField(max_length=20,default="")
    phone = models.CharField(validators = [phone_validate], max_length=10, unique=True)
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=datetime.date.today)    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'id_user','name', 'phone']

    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
        
    def __str__(self):
        return str(self.email)
"""
class Cliente(CustomUser):

    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="usuario_cliente")
    #users = models.OneToOneField(CustomUser,parent_link=True, on_delete=models.CASCADE)

    #photo = models.ImageField('Foto de perfil', upload_to= 'users/photos/', blank=True, null=True)

    biography = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.users)
"""
# ========== Modelo del cliente que contiene un usuario ========== 
class Client(models.Model):
    USER_TYPE_CHOICES = (
      (1, 'natural'),
      (2, 'juridica'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_client = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    interes_mora = models.FloatField()
    category = models.CharField(max_length=10)
    cycle = models.CharField(max_length=10)
    contrat_number = models.IntegerField(unique=True)
    estrato =  models.PositiveSmallIntegerField()
    billing = models.CharField(max_length=10)
    financial_state = models.CharField(max_length=10)

#==========  Modelo del trabajador que extiende de usuario basico ========== 
class Worker(models.Model):
    USER_TYPE_CHOICES = (
      (1, 'admin'),
      (2, 'manager'),
      (3, 'operator'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
