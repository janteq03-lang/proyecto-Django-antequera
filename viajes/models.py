from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.pais}"


class Viajero(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Viaje(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.viajero} a {self.destino}"
