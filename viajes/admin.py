from django.contrib import admin
from .models import Destino, Viajero, Viaje


@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')


@admin.register(Viajero)
class ViajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')


@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('viajero', 'destino', 'fecha')
    list_filter = ('fecha', 'destino')
    search_fields = ('viajero__nombre', 'destino__nombre')
    date_hierarchy = 'fecha'
