from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField(default=00)
    apellido = models.CharField(max_length=25)
    dni = models.CharField(max_length=8, default='00000000')
    procedencia = models.CharField(max_length=25, default='')

    def __str__(self):
        return "{}".format(self.nombre)
