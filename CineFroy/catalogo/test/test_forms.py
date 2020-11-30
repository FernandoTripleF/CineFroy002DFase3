from django.test import TestCase
from peliculas.forms import GeneroForm, MovieForm
from peliculas.models import Cliente, Pelicula
from django.core.files.uploadedfile import SimpleUploadedFile

class ClienteFormsTest(TestCase):
    def test_valid_form(self):
        g = Cliente.objects.create(name='Prueba1', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GeneroForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Cliente.objects.create(name='', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GeneroForm(data=data)
        self.assertFalse(form.is_valid())

class MovieFormsTest(TestCase):
    def test_valid_form(self):
        genre = Cliente.objects.create(name='1', summary='Prueba')
        genre = Cliente.objects.get(pk=1).pk
        m = Pelicula.objects.create(title='Prueba1', summary='Prueba', url='https://www.youtube.com/embed/rslZ-fHiSuI')
        m.save()
        data = {'title': m.title, 'summary': m.summary, 'genre': genre, 'url' : m.url, }
        
        with open('peliculas/static/img/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')
        
        form = MovieForm(data, {'image': document})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Cliente.objects.create(name='Accion', summary='Prueba')
        m = Pelicula.objects.create(title='', summary='Prueba', genre=g, url='https://www.youtube.com/embed/rslZ-fHiSuI')
        data = {'title': m.title, 'summary': m.summary, 'genre': m.genre, 'url' : m.url, }
        form = MovieForm(data=data)
        self.assertFalse(form.is_valid())