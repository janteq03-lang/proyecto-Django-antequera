from django.db import models
from usuarios.models import Usuario


class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.pais}"


class Viaje(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.usuario} a {self.destino}"
