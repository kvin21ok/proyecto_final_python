from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}, {self.numero_pasaporte}, {self.id}'

class Mascota(models.Model):
    nombre = models.CharField(max_length=25)
    tipo = models.CharField(max_length= 25)
    edad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}, {self.tipo}, {self.edad}'

class Empleo(models.Model):
    ocupacion = models.CharField(max_length=25)
    antiguedad = models.IntegerField()
    cargo = models.CharField(max_length=50)
    breve_descripcion = models.CharField(max_length=140)

    def __str__(self):
        return f'{self.ocupacion}, {self.antiguedad}, {self.cargo}'