from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user_perfil(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    nombres = models.CharField(max_length=100, null=True)
    apellidos = models.CharField(max_length=100, null=True )
    cedula = models.CharField(max_length=10, null=True)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=True)
    correo = models.EmailField(null=True)



    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')
    def __str__(self):
        return self.username

