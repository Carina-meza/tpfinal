from django.db import models
from ..usuarios.models import Usuario

# Create your models here.
class Autor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(default='default.jpg', upload_to='autores')
    profesion = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 10000)
    telefono = models.CharField(max_length = 20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario
