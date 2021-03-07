from django.db import models

# Create your models here.

class Rubro(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.IntegerField()
    rubro = models.ForeignKey('Rubro', on_delete = models.CASCADE)
    tamaño = models.IntegerField()
    imagen = models.ImageField(upload_to = 'productos')

    def __str__(self):
        return self.nombre
