from django.db import models

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Reserva(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    huesped = models.CharField(max_length=100)