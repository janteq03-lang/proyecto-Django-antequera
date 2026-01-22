from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'tipo_documento',
        'nro_documento',
        'email',
        'fecha_registro',
    )
    search_fields = ('nombre', 'apellido', 'nro_documento', 'email')
