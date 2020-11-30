from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from Pelicula.models import Genero, Pelicula

class ClienteListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        num_Clientes = 13

        for cliente_id in range(num_Clientes):
            Cliente.objects.create(
                nombre_cli=f'Accion {cliente_id}',
                rut_Clie=f'Prueba {cliente_id}',

            )
