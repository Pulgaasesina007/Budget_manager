from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user_perfil(AbstractUser):
    username = models.CharField(max_length=150, unique=True)


    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')


class Usuario_perfil(models.Model):


    nombres = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100, null=False )
    cedula = models.CharField(max_length=10, null=False)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=False)
    correo = models.EmailField(null=False)

    user= models.OneToOneField(user_perfil,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombres

