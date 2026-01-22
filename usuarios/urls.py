from django.urls import path
from .views import (
    list_usuarios, Detail_usuarios, Create_usuarios, Update_usuarios, Delete_usuarios
)

app_name = 'usuarios'


urlpatterns = [
    path('', list_usuarios.as_view(), name='listar_usuarios'),
    path('crear/', Create_usuarios.as_view(), name='usuario_form'),
    path('<slug:code>/', Detail_usuarios.as_view(), name='usuario_detalle'),
    path('<slug:code>/editar/', Update_usuarios.as_view(), name='usuario_editar'),
    path('<int:pk>/eliminar/', Delete_usuarios.as_view(), name='usuario_eliminar'),
]