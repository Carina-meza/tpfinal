from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
   path('alta/', views.Alta_Categoria.as_view(), name = 'alta_categoria'),
   path('listar/', views.Listar, name = 'listar'),
]