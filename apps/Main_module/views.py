from django.shortcuts import render,HttpResponse,redirect
from .forms import UserRegistrationForm
from .models import Usuario_perfil
def Index(request):
    return  render(request,'inicio.html')
# Create your views here.
def Usuario_r(request):
    if request.method=='GET':
        return  render(request,'Usuario/usuario_r.html',{'form':UserRegistrationForm()})
    else:
          Usuario_perfil.objects.create(
            nomusuario=request.POST['nomusuario'],
            nombres=request.POST['nombres'],
            apellidos=request.POST['apellidos'],
            cedula=request.POST['cedula'],
            telefono=request.POST['telefono'],
            fecha_nacimiento=request.POST['fecha_nacimiento'],
            correo=request.POST['correo'],
            contraseña=request.POST['contraseña'])
    return redirect("/")
def Gastos_Ingreso_modulo(request):
    return render(request,'Gastos_Ingresos_modulo.html')


def Login_usuario(request):
    return render(request,'./Usuario/Login_usuario.html')

def Perfil_usuario(request):
    return render(request,'./Usuario/actualizar_datos.html')
def usuario_act_dat(request):
    return render(request,'./Usuario/actualizar_datos.html')
def cambiar_contraseña(request):
    return  render(request,'./Usuario/cambiar_contraseña.html')