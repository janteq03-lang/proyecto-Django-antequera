from django.shortcuts import render
from .forms import BuscarViajeForm
from .forms import DestinoForm, ViajeroForm, ViajeForm, BuscarViajeForm
from .models import Viaje

def inicio(request):
    return render(request, "viajes/inicio.html")


def crear_destino(request):
    form = DestinoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "viajes/formulario.html", {"form": form, "titulo": "Crear Destino"})


def crear_viajero(request):
    form = ViajeroForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "viajes/formulario.html", {"form": form, "titulo": "Crear Viajero"})


def crear_viaje(request):
    form = ViajeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "viajes/formulario.html", {"form": form, "titulo": "Crear Viaje"})


def buscar_viaje(request):
    form = BuscarViajeForm(request.GET)
    viajes = Viaje.objects.all()

    if request.GET.get("destino"):
        viajes = Viaje.objects.filter(
            destino__nombre__icontains=request.GET.get("destino")
        )

    return render(request, "viajes/buscar.html", {
        "form": form,
        "viajes": viajes
    })
