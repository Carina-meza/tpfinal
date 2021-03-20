from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from apps.usuarios.models import usuario_Nuevo

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class RegistroUsuarioForm2(forms.ModelForm):
	class Meta:
		model = usuario_Nuevo
		fields = ['username', 'email', 'first_name', 'last_name', 'profesion', 'imagen', 'telefono', 'descripcion']
