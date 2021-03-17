from django.db import models
from ..categorias.models import Categoria
from ..usuarios.models import Usuario

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length = 1024)
    descripcion = models.CharField(max_length = 2000)
    contenido = models.TextField(max_length = 10000)
    imagen = models.ImageField(upload_to = 'publicaciones')
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, blank=True, null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    contenido = models.CharField(max_length = 2000)
    publicacion = models.ForeignKey('Publicacion', on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.contenido
