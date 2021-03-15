from django.urls import path
from . import views

app_name = 'publicaciones'

urlpatterns = [
   path('', views.index, name = 'index'),
   path('articulo/<int:pk>', views.PublicacionesDetailView.as_view(), name = 'articulo'),
   path('nueva/', views.Alta_Publicacion.as_view(), name = 'alta_publicacion'),
   path('listar/', views.Listar, name = 'listar'),
   path('prueba/', views.Prueba, name = 'prueba'),
]
