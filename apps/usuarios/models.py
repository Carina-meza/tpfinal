from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(default='default.jpg', upload_to='usuarios', blank=True, null=True)
    profesion = models.CharField(max_length = 50, blank=True, null=True)
    descripcion = models.TextField(max_length = 10000, blank=True, null=True)
    telefono = models.CharField(max_length = 20, blank=True, null=True)
