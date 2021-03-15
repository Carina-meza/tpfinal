from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm

# Create your views here.

class registro(CreateView):
   form_class = RegistroUsuarioForm
   template_name = 'usuarios/registro.html'
   success_url = reverse_lazy('login')