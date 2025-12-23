from django import forms
from .models import Destino, Viajero, Viaje

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'


class ViajeroForm(forms.ModelForm):
    class Meta:
        model = Viajero
        fields = '__all__'


class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = '__all__'


class BuscarViajeForm(forms.Form):
    destino = forms.CharField(
        max_length=50,
        required=False
    )