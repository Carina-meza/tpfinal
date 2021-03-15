from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Publicacion
from .forms import Formulario_Alta_Publicacion


# Create your views here.

def index(request):
   return render(request, 'publicacion/index.html')

class PublicacionesDetailView(DetailView):
   model = Publicacion
   template_name = 'publicacion/ver.html'

class Alta_Publicacion(CreateView):
   model = 'Publicacion'
   form_class = Formulario_Alta_Publicacion
   template_name = 'publicacion/alta_publicacion.html'
   success_url = reverse_lazy('home')

def Listar(request):
   return render(request, 'publicacion/listar.html', {
      'publicaciones': Publicacion.objects.all(),
   })

def Prueba(request):
   return render(request, 'publicacion/prueba.html', {
      'personas': [
         {
            'nombre': 'Juan',
            'edad': 35,
         },
         {
            'nombre': 'Pepe',
            'edad': 20,
         },
      ]
   })
