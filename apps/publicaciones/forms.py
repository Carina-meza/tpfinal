from django import forms
from .models import Publicacion

class Formulario_Alta_Publicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = '__all__'
    def __init__(self, *args, **kwargs):
         self.autor = kwargs.pop('user', None)
         super(Formulario_Alta_Publicacion, self).__init__(*args, **kwargs)