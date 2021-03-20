from django.urls import path
from django.views.decorators.http import require_POST
from . import views

app_name = 'publicaciones'

urlpatterns = [
   path('', views.IndexListView.as_view(), name = 'home'),
   path('ver/<int:pk>', views.PublicacionesDetailView.as_view(), name = 'ver'),
   path('nueva_publicacion/', views.Nueva_Publicacion.as_view(), name = 'nueva_publicacion'),
   path('buscar/', views.BuscarListView.as_view(), name = 'buscar'),
   path('categoria/<int:pk>', views.PubCatListView.as_view(), name = 'publicaciones_categoria'),
   path('comentar/<int:pk>', require_POST(views.Nuevo_Comentario.as_view()), name = 'comentar'),
]
