#from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Register(models.Model):
    nombreUsuario = models.CharField(max_length=50, null=False)
    apellidosUsuario = models.CharField(max_length=50, null=False)
    edadUsuario = models.IntegerField(null=False)
    correoUsuario = models.EmailField(max_length=50, null=False)
    fechaNacimientoUsuario = models.DateField(null=False)
    sexo = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=50, null=False)
