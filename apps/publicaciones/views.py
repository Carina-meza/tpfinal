from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from apps.categorias.models import Categoria
from .models import Publicacion
from .forms import Formulario_Alta_Publicacion


# Create your views here.

'''def index(request):
   return render(request, 'publicacion/index.html', {
      'publicaciones': Publicacion.objects.all(),
   })'''

class IndexListView(ListView):
    model = Publicacion
    context_object_name = 'publicaciones'
    template_name = 'publicacion/index.html'

class BuscarListView(ListView):
   def get_queryset(self):
      if self.request.method == 'GET':
         queryset = Publicacion.objects.all()
         query = self.request.GET.get('q', None)
         if query is not None and query != '':
            queryset = queryset.filter(
               Q(titulo__icontains = query) |
               Q(descripcion__icontains = query) |
               Q(contenido__icontains = query)
            )
         return queryset
   context_object_name = 'publicaciones'
   template_name = 'publicacion/listar.html'

class PubCatListView(ListView):
   def get_queryset(self):
      self.categoria = get_object_or_404(Categoria, id=self.kwargs['pk'])
      return Publicacion.objects.filter(categoria=self.categoria)
   context_object_name = 'publicaciones'
   template_name = 'publicacion/listar.html'

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
