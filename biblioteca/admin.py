from django.contrib import admin
from .models import Libro, Cliente,Genero

class LibroInline(admin.TabularInline):
    model = Libro
    extra = 0
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id","titulo","autor","Genero","imagen")
    list_filter = ("titulo","autor")

class ClienAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido","correo","telefono")
    list_filter = ("nombre",)
    
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id","nombre")
    list_filter = ("nombre",)
    inlines = [LibroInline]
    


# Register your models here.
admin.site.register(Libro,LibroAdmin)
admin.site.register(Cliente,ClienAdmin)
admin.site.register(Genero,GeneroAdmin)