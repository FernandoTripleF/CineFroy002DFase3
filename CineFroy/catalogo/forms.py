from django import forms

from . models import Cliente, Pelicula, Genero

class MovieForm(forms.ModelForm):
    nombre = forms.CharField(label='Titulo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    descripcion = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    url = forms.URLField(label='URL', max_length=100,widget=forms.URLInput(
        attrs={
            'class':'form-control'
        }
    ))
    genero = forms.ModelChoiceField(queryset=Pelicula.objects.all(), label='Género',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))
    image = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))

    class Meta:
        model = Pelicula
        fields = ('nombre','descripcion','genero', 'url', 'image',)

class GeneroForm(forms.ModelForm):
    nombre_cli = forms.CharField(label='Nombre Cliente',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    rut_cli = forms.CharField(label='rut Cliente', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Cliente
        fields = ('nombre_cli', 'rut_cli',)