from django.urls import path
from django.contrib.auth import views as auth
from . import views

app_name = 'usuarios'

urlpatterns = [
	path('emprendedores/', views.UsuEmpListView.as_view(), name = 'emprendedores'),
	path('perfil/', views.perfil.as_view(), name='perfil'),
    path('registro/', views.registro.as_view(), name='registro'),
    path('login/', auth.LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path('logout/', auth.LogoutView.as_view(), name="logout")
]