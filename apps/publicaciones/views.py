from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.categorias.models import Categoria
from .models import Publicacion, Comentario
from .forms import Formulario_Publicacion, Formulario_Nuevo_Comentario, Formulario_Buscar

# Create your views here.

class IndexListView(ListView):
   model = Publicacion
   context_object_name = 'publicaciones'
   template_name = 'publicacion/index.html'

class BuscarListView(ListView):
   def get_queryset(self):
      if self.request.method == 'GET':
         query = self.request.GET.get('q', None)
         desde = self.request.GET.get('desde', None)
         hasta = self.request.GET.get('hasta', None)
         queryset = Publicacion.objects.all()
         if query is not None and query != '':
            queryset = queryset.filter(
               Q(titulo__icontains = query) |
               Q(descripcion__icontains = query) |
               Q(contenido__icontains = query)
            )
         if desde is not None and desde != '':
            queryset = queryset.filter(fecha__gte = desde)
         if hasta is not None and hasta != '':
            queryset = queryset.filter(fecha__lte = hasta)
         return queryset
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
         'form': Formulario_Buscar(self.request.GET),
      })
      return context
   context_object_name = 'publicaciones'
   template_name = 'publicacion/buscar.html'

class PubCatListView(ListView):
   def get_queryset(self):
      self.categoria = get_object_or_404(Categoria, id=self.kwargs['pk'])
      return Publicacion.objects.filter(categoria=self.categoria)
   context_object_name = 'publicaciones'
   template_name = 'publicacion/listar.html'

class PublicacionesDetailView(DetailView):
   model = Publicacion
   template_name = 'publicacion/ver.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
         'form': Formulario_Nuevo_Comentario(),
         'comentarios': Comentario.objects.filter(publicacion=context['publicacion']),
      })
      return context

class Nueva_Publicacion(LoginRequiredMixin, CreateView):
   form_class = Formulario_Publicacion
   template_name = 'publicacion/nueva.html'
   success_url = reverse_lazy('publicaciones:mis_publicaciones')
   def form_valid(self, form):
      form.instance.autor = self.request.user
      return super().form_valid(form)

class Editar_Publicacion(LoginRequiredMixin, UpdateView):
   form_class = Formulario_Publicacion
   template_name = 'publicacion/editar.html'
   success_url = reverse_lazy('publicaciones:mis_publicaciones')
   def get_object(self, queryset=None):
      return get_object_or_404(Publicacion, id=self.kwargs['pk'])

class Eliminar_Publicacion(DeleteView): 
   model = Publicacion
   template_name = 'publicacion/confirmar.html'
   success_url = reverse_lazy('publicaciones:mis_publicaciones')

class Mis_Publicaciones(ListView):
   def get_queryset(self):
      return Publicacion.objects.filter(autor=self.request.user)
   context_object_name = 'publicaciones'
   template_name = 'publicacion/mispublicaciones.html'

class Nuevo_Comentario(CreateView):
   form_class = Formulario_Nuevo_Comentario
   def get_success_url(self):
      return reverse_lazy('publicaciones:ver', kwargs={'pk': self.kwargs['pk']})
   def form_valid(self, form):
      form.instance.publicacion = get_object_or_404(Publicacion, id=self.kwargs['pk'])
      form.instance.usuario = self.request.user
      return super().form_valid(form)
