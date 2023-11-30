from django.db import models

# Create your models here.

class User(models.Model):

    nomusuario = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100, null=False )
    cedula = models.CharField(max_length=10, null=False)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=False)
    correo = models.EmailField(null=False)
    contraseña = models.CharField(max_length=100, null=False)



