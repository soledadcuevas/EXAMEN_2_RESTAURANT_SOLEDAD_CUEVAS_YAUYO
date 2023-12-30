from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    dni = models.CharField(max_length=8, default='00000000')
