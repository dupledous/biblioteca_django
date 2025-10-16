from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('catalogo/',views.buscar_libro, name="catalogo"),
    #path("contacto/",views.contacto, name="contacto"),
    path("catalogo/",views.catalogo, name="catalogo"),
    path("clientes/",views.ClienteListView.as_view(), name="clientes"),
    path("libros/",views.LibroListView.as_view(), name="libros"),
    path("generos/",views.GeneroListView.as_view(), name="generos"),
    path("clientes/<int:pk>",views.ClienteDetailView.as_view(), name="cliente-detail"),
    path("libros/<int:pk>",views.LibroDetailView.as_view(), name="libro-detail"),
    path("clientes/add/",views.ClienteCreateView.as_view(), name="cliente-add"),
     path('register/', views.register, name='register')
]
