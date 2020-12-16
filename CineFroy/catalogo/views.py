from django.shortcuts import render
from . models import Pelicula, Cliente, Genero
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    num_Pelis = Pelicula.objects.all().count()

    num_Clientes = Cliente.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_Pelis': num_Pelis,'num_Clientes': num_Clientes},
    )

def cartelera(request):
    Pelis = Pelicula.objects.all()

    return render(
        request,
         'cartelera.html',
        context={'Pelis': Pelis},
    )

def formulario(request):

        return render(
        request,
         'formulario.html',
          )


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'

    def get_success_url(self):
    # find your next url here

        next_url = self.request.POST.get('next',None) # here method should be GET or POST.
        if next_url:
            return "%s" % (next_url) # you can include some query strings as well
        else :
            return reverse_lazy('index') # what url you wish to return

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'

class ClienteDelete(DeleteView):
    model = Cliente
    succes_url = reverse_lazy('cliente')

class ClienteDetailView(generic.DetailView):
    model = Cliente


class PeliculaCreate(CreateView):
    model = Pelicula
    fields = '__all__'

    def get_success_url(self):
    # find your next url here

        next_url = self.request.POST.get('next',None) # here method should be GET or POST.
        if next_url:
            return "%s" % (next_url) # you can include some query strings as well
        else :
            return reverse_lazy('index') # what url you wish to return


class PeliculaUpdate(UpdateView):
    model = Pelicula
    fields = '__all__'

class PeliculaDelete(DeleteView):
    model = Pelicula
    succes_url = reverse_lazy('cliente')

class PeliculaDetailView(generic.DetailView):
    model = Pelicula



