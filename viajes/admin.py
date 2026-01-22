from django.contrib import admin
from .models import Destino, Viaje


@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')


@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'destino', 'fecha')
