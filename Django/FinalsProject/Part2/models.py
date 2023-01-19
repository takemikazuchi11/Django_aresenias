from django.db import models

# Create your models here.

class Registration(models.Model):
    id= models.AutoField(primary_key=True)
    uname= models.CharField(max_length=25)
    email= models.CharField(max_length=50)
    password= models.CharField(max_length=255)
    fname = models.CharField(max_length=50)
    mname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    phone= models.CharField(max_length=13)

class RegistrationManager(models.Manager):
    pass