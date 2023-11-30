from django.db import models

# Create your models here.

class User(models.Model):
    idusuario = models.IntegerField(primary_key=True, unique=True)
    nomusuario = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100, null=False )
    cedula = models.CharField(max_length=10, null=False)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=False)
    correo = models.EmailField(null=False)
    contraseña = models.CharField(max_length=100, null=False)

    def _str_(self):
        return f'{self.nomusuario}'

class Tipo_Ingreso(models.Model):
    idTipoIngreso = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)

class Ingresos(models.Model):
    idingreso = models.IntegerField(primary_key=True, unique=True)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now=True)
    valor = models.FloatField()
    tipoIngreso = models.ForeignKey(Tipo_Ingreso, on_delete=models.PROTECT)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class Tipo_Gasto(models.Model):
    idTipoGasto = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)

class Gastos(models.Model):
    idgasto = models.IntegerField(primary_key=True, unique=True)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now=True)
    valor = models.FloatField()
    tipoGasto = models.ForeignKey(Tipo_Gasto, on_delete=models.PROTECT)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)



class Historial(models.Model):
    idhistorial = models.IntegerField(primary_key=True, unique=True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    ingreso = models.ForeignKey(Ingresos, on_delete=models.RESTRICT)
    gasto = models.ForeignKey(Gastos, on_delete=models.RESTRICT)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    total = models.FloatField()

class Preferencias(models.Model):
    idpreferencia = models.IntegerField(primary_key=True, unique=True)
    descripcion = models.TextField()

class Usuario_Preferencia(models.Model):
    idUsuarioPreferencia = models.IntegerField(primary_key=True, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    preferencia = models.ForeignKey(Preferencias, on_delete=models.RESTRICT)

class Predicciones(models.Model):
    idprediccion = models.IntegerField(primary_key=True, unique=True)
    usuario_preferencia = models.ForeignKey(Usuario_Preferencia, on_delete=models.RESTRICT)
    fecha = models.DateField()
    descripcion = models.TextField()