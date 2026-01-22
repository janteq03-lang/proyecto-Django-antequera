from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'tipo_documento',
            'nro_documento',
            'email',
            'telefono',
        ]
       
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Pérez'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'nro_documento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Solo números'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nombre@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 11 1234 5678'}),
        }