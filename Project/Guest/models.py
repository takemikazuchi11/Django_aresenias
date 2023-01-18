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
    email= models.CharField(max_length=20)
    password= models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

    class Meta:
        db_table = "guest_register"

  

class empAuth_object(models.Manager):
    pass

class bookForm(models.Model):
    id= models.AutoField(primary_key=True)
    fname= models.CharField(max_length=25)
    contactno= models.CharField(max_length=13)
    packages= models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time= models.CharField(max_length=50)
    add= models.CharField(max_length=250)
    
class bookFormManager(models.Manager):
    pass