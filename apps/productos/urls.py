from django.urls import path
from . import views

app_name = 'productos'
<<<<<<< HEAD
=======

>>>>>>> 57f8ee464ae588a86962207373b2250c0e558d78
urlpatterns = [
   path('ALTA_P/', views.Alta_Producto.as_view(), name = 'cargar_p'),
   path('ALTA_R/', views.Alta_Rubro.as_view(), name = 'cargar_r'),
   path('Listar/', views.Listar, name = 'listar')   
]