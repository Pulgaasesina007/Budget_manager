from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.Index),
    path('Home/Gastos_Ingreso_modulo/', views.Gastos_Ingreso_modulo),
    path('actualizar_datos/', views.usuario_act_dat),
    path('Home/Perfil_usuario/cambiar_contraseña/', views.cambiar_contraseña),
    path('registro_usuario/', views.registro),
    path('Home/Perfil_usuario/',views.Perfil_usuario),
    path('',views.Login_usuario)
]