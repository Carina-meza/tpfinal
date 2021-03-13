from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publicacion

# Create your views here.

def index(request):
   return render(request, 'blog/index.html')

class PublicacionesDetailView(DetailView):
    model = Publicacion
    template_name = 'blog/ver.html'

   