from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
	path('emprendedores/', views.UsuEmpListView.as_view(), name = 'emprendedores'),
]