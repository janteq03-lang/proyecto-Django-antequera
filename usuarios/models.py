from django.db import models
import uuid

def generar_code():
    return uuid.uuid4().hex

class Usuario(models.Model):
    TIPO_DOCUMENTO = (
        ('DNI', 'DNI'),
        ('PAS', 'Pasaporte'),
        ('CED', 'Cedula'),
    )

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO)
    nro_documento = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    code = models.CharField(
        max_length= 16,
        unique= True,
        default= generar_code
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.nro_documento})"
