from django.db import models

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=10)
    anio= models.CharField(max_length=10)
    hoy= models.CharField(max_length=30)
    profecion = models.CharField(max_length=30)
    parentesco= models.CharField(max_length=30)
    Telequino = models.CharField(max_length=30)
    hoy= models.CharField(max_length=30)
    
