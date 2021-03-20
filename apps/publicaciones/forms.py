from django import forms
from .models import Publicacion, Comentario

class Formulario_Publicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ['autor']

class Formulario_Nuevo_Comentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
