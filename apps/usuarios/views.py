from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm, RegistroUsuarioForm2 
from .models import usuario_Nuevo

# Create your views here.

class registro(CreateView):
   form_class = RegistroUsuarioForm
   template_name = 'usuarios/registro.html'
   success_url = reverse_lazy('registrodos')

class registro2(CreateView):
	model = 'usuario_Nuevo'
	form_class = RegistroUsuarioForm2
	template_name = 'usuarios/registroparte2.html'
	success_url = reverse_lazy('login')