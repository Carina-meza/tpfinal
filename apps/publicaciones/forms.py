from django import forms
from .models import Publicacion, Comentario

class DateInput(forms.DateInput):
    input_type = 'date'

class Formulario_Publicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ['autor']

class Formulario_Nuevo_Comentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        labels = {'contenido': 'Comentario'}
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control'})
        }

class Formulario_Buscar(forms.Form):
    q = forms.CharField(max_length=50, label= 'Buscar', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    desde = forms.DateField(widget=DateInput(), required=False)
    hasta = forms.DateField(widget=DateInput(), required=False)
