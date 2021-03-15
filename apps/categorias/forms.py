from django import forms
from .models import Categoria

class Formulario_Alta_Categoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
