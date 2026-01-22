from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('destino/', views.crear_destino, name='crear_destino'),
    path('viaje/', views.crear_viaje, name='crear_viaje'),
    path('buscar/', views.buscar_viaje, name='buscar_viaje'),
    path('detalle/<int:pk>/', views.detalle_viaje, name='detalle_viaje'),
    path('viaje/editar/<int:pk>/', views.actualizar_viaje, name='editar_viaje'),
    path('viaje/eliminar/<int:pk>/', views.eliminar_viaje, name='eliminar_viaje'),
]