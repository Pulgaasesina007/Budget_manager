from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('Home/', views.Index, name='Home'),
    path('Home/Gastos_Ingreso_modulo/', views.Gastos_Ingreso_modulo),
    path('actualizar_datos/', views.usuario_act_dat),
    path('Home/Perfil_usuario/cambiar_contraseña/', views.cambiar_contraseña),
    path('Usuario_r/',views.Usuario_r,name = 'Usuario_r'),
    path('Home/Perfil_usuario/',views.Perfil_usuario),
    path('',views.login_usuario, name = 'login_usuario'),
    path('login/', LogoutView.as_view(template_name='Usuario/Login_usuario.html'), name='logout')

]