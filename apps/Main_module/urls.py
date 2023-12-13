from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .views import cerrar_sesion_view

urlpatterns = [
    path('Home/', views.Index, name='Home'),
<<<<<<< HEAD
    path('Home/Gastos_Ingreso_modulo/', views.Gastos_Ingreso_modulo, name= 'Ingreso_modulo'),
    path('actualizar_datos/', login_required(views.usuario_act_dat),name='usuario_act_dat'),
    path('Home/Perfil_usuario/cambiar_contraseña/', login_required(views.act_password),name = 'act_password'),
    path('Usuario_r/',views.Usuario_r,name = 'Usuario_r'),
    path('Home/Perfil_usuario/',login_required(views.Perfil_usuario), name='Perfil_usuario'),
    path('',views.login_usuario, name = 'login_usuario'),
    path('login/', LogoutView.as_view(template_name='Usuario/Login_usuario.html'), name='logout')
=======
    path('Home/Gastos_Ingreso_modulo/', views.Gastos_Ingreso_modulo, name='Ingreso_modulo'),
    path('actualizar_datos/', login_required(views.usuario_act_dat), name='usuario_act_dat'),
    path('Home/Perfil_usuario/cambiar_contraseña/', views.cambiar_contraseña),
    path('Usuario_r/', views.Usuario_r, name='Usuario_r'),
    path('Home/Perfil_usuario/', login_required(views.Perfil_usuario), name='Perfil_usuario'),
    path('', views.login_usuario, name='login_usuario'),
    path('login/', LogoutView.as_view(template_name='Usuario/Login_usuario.html'), name='logout'),  # Agregar coma aquí
    path('cerrar_sesion/', cerrar_sesion_view, name='cerrar_sesion'),
]
>>>>>>> d850c57533fc884832d39eb829a67cb81e7cbc5c

