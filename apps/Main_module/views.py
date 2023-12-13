from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import Register_User,Login_user,CambiarContraseñaForm
from .models import user_perfil
from django.contrib.auth import authenticate, login

def Index(request):
    return  render(request,'inicio.html')
# Create your views here.

def Usuario_r(request):
    if request.method == 'POST':
        print("POST a")
        form = Register_User(request.POST)
        if form.is_valid():
            if user_perfil.objects.filter(username=form.cleaned_data['username']).exists():
                print("usuario ya existe")
                form.add_error('username', 'Este usuario ya existe')
            else:
                print("login")
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('/Home')
        else:
            print(form.errors)
            print("error form no valido ")
    else:
        form = Register_User()  # Mover la inicialización del formulario fuera del bloque 'if'
    return render(request, 'Usuario/usuario_r.html', {'form': form})
def Gastos_Ingreso_modulo(request):
    return render(request,'Gastos_Ingresos_modulo.html')


def login_usuario(request):
    mensaje_error = ''

    print("Entrando a la vista de login")

    if request.method == 'POST':
        print("Método POST recibido")
        print(request.POST)  # Imprime el contenido del formulario

        form = Login_user(request, request.POST)

        if form.is_valid():
            print("Formulario válido")

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print(f"Username: {username}")
            print(f"Password: {password}")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(f"Usuario autenticado: {user.username}")

                login(request, user)

                next_url = request.POST.get('next') or 'Home/'
                return redirect(next_url)

            else:
                print("Error autenticando usuario")
                mensaje_error = "Credenciales inválidas"

        else:
            print("Formulario no válido")
            print(form.errors)

    else:
        print("Petición GET recibida")
        form = Login_user()

    return render(request, 'Usuario/Login_usuario.html', {'form': form, 'mensaje_error': mensaje_error, 'next': request.GET.get('next', '')})

def Perfil_usuario(request):
    perfil = get_object_or_404(user_perfil, username=request.user.username)
    print(perfil)
    return render(request, 'Usuario/Perfil_user.html', {'datos': perfil})

def usuario_act_dat(request):
    perfil= get_object_or_404(user_perfil,username=request.user.username)

    return render(request,'./Usuario/actualizar_datos.html',   {
        'perfil': perfil
    })


def act_password(request):
    perfil = get_object_or_404(user_perfil, username=request.user.username)

    if request.method == 'POST':
        form = CambiarContraseñaForm(request.POST)

        if form.is_valid():
            password1 = form.cleaned_data['password1']

            # Actualizar la contraseña del usuario
            request.user.set_password(password1)
            request.user.save()
            next_url = request.POST.get('next') or 'logout'
            return redirect(next_url)

    else:
        form = CambiarContraseñaForm()

    return render(request, './Usuario/cambiar_contraseña.html', {'form': form, 'perfil': perfil})