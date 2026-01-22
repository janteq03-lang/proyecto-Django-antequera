from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import (
    DestinoForm,
     ViajeForm,
    BuscarViajeForm,
     ViajeUpdateForm,
)

from .models import Viaje


def inicio(request):
    return render(request, "viajes/inicio.html")

@login_required
def crear_destino(request):
    if request.method == "POST":
        form = DestinoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Destino creado correctamente")
            return redirect("crear_destino")
    else:
        form = DestinoForm()

    return render(request, "viajes/formulario.html", {"form": form})



@login_required
def crear_viaje(request):
    if request.method == "POST":
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Viaje creado correctamente")
            return redirect("crear_viaje")
    else:
        form = ViajeForm()

    return render(request, "viajes/formulario.html", {"form": form})

@login_required
def buscar_viaje(request):
    form = BuscarViajeForm(request.GET or None)
    viajes = Viaje.objects.all()

    if form.is_valid():
        destino = form.cleaned_data.get("destino")
        if destino:
            viajes = viajes.filter(destino__nombre__icontains=destino)

    return render(request, "viajes/buscar.html", {
        "form": form,
        "viajes": viajes
    })

@login_required
def detalle_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    return render(request, "viajes/detalle.html", {"viaje": viaje})

@login_required
def actualizar_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)

    if request.method == "POST":
        form = ViajeUpdateForm(request.POST, instance=viaje)
        if form.is_valid():
            form.save()
            messages.success(request, "Viaje actualizado correctamente")
            
            return redirect("detalle_viaje", pk=viaje.pk) 
    else:
        form = ViajeUpdateForm(instance=viaje)

    return render(request, "viajes/formulario.html", {"form": form})


@login_required
def eliminar_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    if request.method == 'POST':
        viaje.delete()
        messages.success(request, "Viaje eliminado correctamente")
        return redirect("buscar_viaje")

    return render(request, 'viajes/eliminar_viaje.html', {'viaje': viaje})