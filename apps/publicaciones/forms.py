from django import forms
from .models import Publicacion

class Formulario_Alta_Publicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        #fields = ['titulo', 'contenido', 'imagen', 'categoria']
        exclude = ['autor']
