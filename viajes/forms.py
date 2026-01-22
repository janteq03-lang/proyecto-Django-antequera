from django import forms
from django.utils import timezone
from .models import Viaje, Destino
from datetime import timedelta

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ['nombre', 'pais']
        
        widgets = {
            'nombre': forms.TextInput (attrs={'class': 'form-control'}),
            'pais': forms.TextInput (attrs={'class': 'form-control'})
        }



class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['destino', 'usuario', 'fecha', 'descripcion']
        widgets = {
            'destino': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}
            ),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        ahora = timezone.now()
        limite = ahora + timedelta(days=365)

        if fecha < ahora:
            raise forms.ValidationError(
                "La fecha y hora no pueden ser anteriores al momento actual."
            )

        if fecha > limite:
            raise forms.ValidationError(
                "La fecha no puede superar los 12 meses."
            )

        return fecha

class ViajeUpdateForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['fecha', 'descripcion']
        widgets = {
            'fecha': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}
            ),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']

        
        if self.instance.pk and fecha == self.instance.fecha:
            return fecha

        ahora = timezone.now()
        limite = ahora + timedelta(days=365)

        if fecha < ahora:
            raise forms.ValidationError(
                "La fecha y hora no pueden ser anteriores al momento actual."
            )

        if fecha > limite:
            raise forms.ValidationError(
                "La fecha no puede superar los 12 meses."
            )

        return fecha


class BuscarViajeForm(forms.Form):
    destino = forms.CharField(
        max_length=50,
        required=False
    )