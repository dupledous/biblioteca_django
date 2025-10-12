from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, help_text="ingresar tu nombre")
    apellido = models.CharField(max_length=50 , help_text="ingresar tu apellido")
    correo = models.EmailField(null=True, blank=True, help_text="engresa tu correo")
    telefono = models.IntegerField()
    class Meta:
        db_table = "Clente"
    def __str__(self):
        return f"{self.nombre}, {self.apellido},{self.correo},{self.telefono}"
    
class Libro(models.Model):
    titulo = models.CharField(max_length=30, help_text="titulo del libro")
    autor = models.CharField(max_length=30, help_text="el autor")
    Genero = models.ForeignKey("Genero", on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="libro",null=True)
    class Meta:
        db_table = "Libro"
        
    def __str__(self):
        return f"{self.titulo}, {self.autor},{self.Genero}"
        
class Genero(models.Model):
    nombre = models.CharField(max_length=50, help_text="genero del libro")
    def __str__(self):
        return f"{self.nombre}"