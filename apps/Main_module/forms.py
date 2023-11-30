from django import forms

class UserRegistrationForm(forms.Form):
    nombres = forms.CharField(
        label='Nombres',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'Nombres'}),
    )
    apellidos = forms.CharField(
        label='Apellidos',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'apellidos'}),
    )
    cedula = forms.CharField(
        label='Cédula',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'cedula'}),
    )
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.TextInput(attrs={'class': 'fechanac'}),
    )
    correo = forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={'class': 'correo'}),
    )
    telefono = forms.CharField(
        label='Telefono',
        widget=forms.TextInput(attrs={'class': 'telefono'}),
    )
    nomusuario = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'nombreusuario'}),
    )
    contraseña = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'contraseña'}),
    )
    confirmacion = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'confirmarcontra'}),
    )

