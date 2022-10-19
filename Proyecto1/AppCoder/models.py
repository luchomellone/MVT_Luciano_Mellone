from django.db import models
from datetime import datetime

class Familia(models.Model) :

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField(null=True)