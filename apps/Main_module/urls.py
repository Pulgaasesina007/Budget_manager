from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('Home/', views.Index),
    path('Home/Gastos_Ingreso_modulo/', views.Gastos_Ingreso_modulo),
    path('actualizar_datos/', views.usuario_act_dat),
    path('Home/Perfil_usuario/cambiar_contraseña/', views.cambiar_contraseña),
    path('Usuario_r/',views.Usuario_r),
    path('Home/Perfil_usuario/',views.Perfil_usuario),
    path('',views.Login_usuario),
    path('admin/',admin.site.urls)
]