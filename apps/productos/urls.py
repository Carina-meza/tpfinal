from django.urls import path
from . import views

app_name = 'productos'
urlpatterns = [
   path('ALTA_P/', views.Alta_Producto.as_view(), name = 'cargar_p'),
   path('ALTA_R/', views.Alta_Rubro.as_view(), name = 'cargar_r'),
   path('Listar/', views.Listar, name = 'listar')   
]