from django.urls import path
from . import views

app_name = 'publicaciones'

urlpatterns = [
   path('', views.index, name = 'index'),
   path('articulo/<int:pk>', views.PublicacionesDetailView.as_view(), name = 'articulo'),
]