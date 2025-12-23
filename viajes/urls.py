from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('destino/', crear_destino),
    path('viajero/', crear_viajero),
    path('viaje/', crear_viaje),
    path('buscar/', buscar_viaje),
]
