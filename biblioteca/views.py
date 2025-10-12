from django.shortcuts import render
from django.views import generic
from .models import Cliente,Libro,Genero
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy




def index(request):
    return render(request, "biblioteca/index.html")

#def contacto(request):
    #return render(request, "biblioteca/contacto.html")

def catalogo(request):
    cant_libros = Libro.objects.all()
    nombre="100 años de soledad"
    autor="gabriel garcia"
    nombre1="Las almas muertas"
    autor1="Nicolai Gogol"
    contexto={"titulo":nombre, "autor":autor, "titulo1":nombre1, "autor1":autor1}
    return render(request, "biblioteca/catalogo.html", contexto)

    
class ClienteListView(generic.ListView):
    model = Cliente
    
class ClienteDetailView(generic.DetailView):
    model= Cliente
    
class LibroListView(generic.ListView):
    model = Libro
    paginate_by = 1
    
class LibroDetailView(generic.DetailView):
    model = Libro
    
class GeneroListView(generic.ListView):
    model = Genero
    
class GeneroDetailView(generic.DetailView):
    model = Genero
    
class ClienteCreateView(CreateView):
    model= Cliente
    fields='__all__'
    template_name ='biblioteca/cliente_form.html'
    success_url = reverse_lazy('clientes')