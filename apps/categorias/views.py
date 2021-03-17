from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Categoria
from .forms import Formulario_Alta_Categoria

# Create your views here.

class Alta_Categoria(CreateView):
   model = 'Categoria'
   form_class = Formulario_Alta_Categoria
   template_name = 'categoria/alta_categoria.html'
   success_url = reverse_lazy('publicaciones:home')
