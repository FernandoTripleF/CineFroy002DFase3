from django.contrib import admin
from . models import Pelicula, Cliente, Genero

# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Cliente)
admin.site.register(Genero)
