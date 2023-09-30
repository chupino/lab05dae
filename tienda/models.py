from django.db import models
from django.db.models import F



class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    def aumentar(modeladmin, request, queryset):
        queryset.update(precio=F('precio') + 10)

    aumentar.short_description = "Aumentar"
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date_published')
    actions = [aumentar]
    actions_on_bottom = True

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombres = models.CharField(max_length=200) 
    apellidos = models.CharField(max_length=200) 
    dni = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200) 
    email = models.EmailField(null=False) 
    fecha_nacimiento = models.DateField() 
    fecha_publicacion = models.DateTimeField()

    def __str__ (self) -> str:
        return self.nombres + self.apellidos


