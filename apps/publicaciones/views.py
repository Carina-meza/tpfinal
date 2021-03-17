from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Publicacion
from .forms import Formulario_Alta_Publicacion


# Create your views here.

def index(request):
   return render(request, 'publicacion/index.html', {
      'publicaciones': Publicacion.objects.all(),
   })

def listar(request):
   return render(request, 'publicacion/listar.html', {
      'publicaciones': Publicacion.objects.all(),
   })

class PublicacionesDetailView(DetailView):
   model = Publicacion
   template_name = 'publicacion/ver.html'

class Nueva_Publicacion(CreateView):
   form_class = Formulario_Alta_Publicacion
   template_name = 'publicacion/nueva.html'
   success_url = reverse_lazy('publicaciones:home')
   def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
