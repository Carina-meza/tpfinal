from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'first_name', 'last_name', 'profesion', 'imagen', 'telefono', 'descripcion']
