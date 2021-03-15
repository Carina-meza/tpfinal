from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 2000)
    imagen = models.ImageField(upload_to = 'categoría')

    def __str__(self):
        return self.nombre
