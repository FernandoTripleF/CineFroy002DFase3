from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cartelera/', views.cartelera, name='cartelera'),
    path('formulario/', views.formulario, name='formulario'),
    path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('pelicula/<str:pk>,', views.PeliculaDetailView.as_view(), name='pelicula-detail'),
    
]

urlpatterns+=[
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
    path('pelicula/create/', views.PeliculaCreate.as_view(), name='pelicula_create'),
    path('pelicula/<str:pk>/update/', views.PeliculaUpdate.as_view(), name='pelicula_update'),
    path('pelicula/<str:pk>/delete/', views.PeliculaDelete.as_view(), name='pelicula_delete'),
    
]