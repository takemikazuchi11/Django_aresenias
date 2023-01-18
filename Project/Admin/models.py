from django.db import models

# Create your models here.

class services(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=25)
    discount= models.CharField(max_length=10)
    price= models.CharField(max_length=50)
    details = models.CharField(max_length=250)
    
class serviceManager(models.Manager):
    pass

class register(models.Model):
    id= models.AutoField(primary_key=True)
    uname= models.CharField(max_length=25)
    email= models.CharField(max_length=10)
    password= models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.uname

    empAuth_object = models.Manager()
