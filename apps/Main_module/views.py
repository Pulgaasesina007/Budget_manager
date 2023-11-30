from django.shortcuts import render

def Index(request):
    return  render(request,'inicio.html')
# Create your views here.

def Gastos_Ingreso_modulo(request):
    return render(request,'Gastos_Ingresos_modulo.html')

def registro(request):
    return  render(request,'./Usuario/registro.html'),

def Login_usuario(request):
    return render(request,'./Usuario/Login_usuario.html')

def Perfil_usuario(request):
    return render(request,'./Usuario/actualizar_datos.html')
def usuario_act_dat(request):
    return render(request,'./Usuario/actualizar_datos.html')
def cambiar_contraseña(request):
    return  render(request,'./Usuario/cambiar_contraseña.html')