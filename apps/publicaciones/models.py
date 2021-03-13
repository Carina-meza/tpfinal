from django.db import models
from ..categorias.models import Categoria
from ..usuarios.models import Usuario
from ..autores.models import Autor

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length = 1024)
    subtitulo = models.CharField(max_length = 1024)
    contenido = models.TextField(max_length = 10000)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Imagen(models.Model):
    titulo = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 2000)
    imagen = models.ImageField(upload_to = 'publicaciones')
    publicacion = models.ForeignKey('Publicacion', on_delete = models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.imagen

class Comentario(models.Model):
    contenido = models.TextField(max_length = 2000)
    publicacion = models.ForeignKey('Publicacion', on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    respuesta = models.ForeignKey('Comentario', on_delete = models.CASCADE, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.contenido
