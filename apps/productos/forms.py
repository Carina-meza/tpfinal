from django import forms
from .models import Producto, Rubro

class Formulario_Alta_Producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class Formulario_Alta_Rubro(forms.ModelForm):
    class Meta:
        model = Rubro
        fields = '__all__'
