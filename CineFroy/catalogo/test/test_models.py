from django.test import TestCase
from . models import Pelicula, Genero, Cliente


class PeliculaTestCase(TestCase):

    def setUp(self):
        a1=Cliente.objects.create(nombre_cliente="Roberto")
        a2=Cliente.objects.create(nombre_cliente="Maria")
        Pelicula.objects.create(nombre="La pesadilla", genero="Accion")
        Pelicula.objects.create(nombre="La noche del demonio", genero="Suspenso")

    