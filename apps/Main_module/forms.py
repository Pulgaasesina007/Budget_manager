from django import forms


class UserRegistrationForm(forms.Form):
    nombres = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'nombres',
        'placeholder': 'Ingrese sus nombres',
    }))

    apellidos = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'apellidos',
        'placeholder': 'Ingrese sus apellidos',
    }))

    cedula = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'cedula',
        'placeholder': 'Ingrese su cédula',
    }))

    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'fechanac',
        'placeholder': 'Fecha de nacimiento',
    }))

    correo = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'correo',
        'placeholder': 'Ingrese su correo electrónico',
    }))

    telefono = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'telefono',
        'placeholder': 'Ingrese su teléfono',
    }))

    nomusuario = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'nombreusuario',
        'placeholder': 'Ingrese su nombre de usuario',
    }))

    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'contraseña',
        'placeholder': 'Ingrese su contraseña',
    }))

    confirmacion = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'confirmarcontra',
        'placeholder': 'Confirme su contraseña',
    }))