from django.urls import path
from . import views

app_name = 'publicaciones'

urlpatterns = [
   path('', views.index, name = 'home'),
   path('ver/<int:id>', views.PublicacionesDetailView.as_view(), name = 'ver'),
   path('nueva_publicacion/', views.Nueva_Publicacion.as_view(), name = 'nueva_publicacion'),
   path('publicaciones/', views.listar, name = 'publicaciones'),
]
