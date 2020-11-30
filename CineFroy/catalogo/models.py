from django.db import models
from django.urls import reverse 
import uuid

# Create your models here.
class Genero(models.Model):
    tipo_genero = models.CharField(max_length=100)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.tipo_genero

class Pelicula(models.Model):
    nombre=models.CharField(max_length=200)
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)
    descripcion=models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='pelis', blank=True, null=True)
    precio = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre_cli=models.CharField(max_length=200)
    rut_cli=models.CharField(max_length=9)

    def __str__(self):
        return self.rut_cli
