from django.db import models

# Create your models here.

class Meseros(models.Model):
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=27, default='')
    dni = models.CharField(max_length=8, default='00000000')

    def __str__(self):
        return "{}".format(self.nombre)