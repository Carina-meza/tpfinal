from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm, PerfilUsuarioForm 
from .models import Usuario

# Create your views here.

class registro(CreateView):
   form_class = RegistroUsuarioForm
   template_name = 'usuarios/registro.html'
   success_url = reverse_lazy('login')

class pefil(UpdateView):
   form_class = PerfilUsuarioForm
   template_name = 'usuarios/pefil.html'
   success_url = reverse_lazy('publicaciones:home')
   def get_object(self, queryset=None):
      return self.request.user
