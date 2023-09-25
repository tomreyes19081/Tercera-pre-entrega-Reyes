from django.db import models

# Create your models here.
class Sedan(models.Model):
    marca= models.CharField(max_length=40)
    modelo= models.CharField(max_length=30)
    fechacompra= models.DateField()

class Coupe(models.Model):
    marca= models.CharField(max_length=40)
    modelo= models.CharField(max_length=30)
    fechacompra= models.DateField()
    
class Suv(models.Model):
    marca= models.CharField(max_length=40)
    modelo= models.CharField(max_length=30)
    fechacompra= models.DateField()


