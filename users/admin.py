from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Perfil


class PerfilAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Extra', {'fields': ('avatar', 'pais', 'fecha_nacimiento', 'direccion')}),
    )

admin.site.register(Perfil, PerfilAdmin)