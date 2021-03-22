from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm, PerfilUsuarioForm 
from .models import Usuario

# Create your views here.

class registro(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('usuarios:login')

class perfil(UpdateView):
    form_class = PerfilUsuarioForm
    template_name = 'usuarios/perfil.html'
    success_url = reverse_lazy('publicaciones:home')
    def get_object(self, queryset=None):
        return self.request.user

class UsuEmpListView(ListView):
    model = Usuario
    context_object_name = 'usuarios'
    template_name = 'usuarios/emprendedores.html'
