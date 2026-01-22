from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import Perfil
from django.utils import timezone

class PerfilCreationForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = Perfil
        fields = UserCreationForm.Meta.fields + (
            'pais',
            'fecha_nacimiento',
            'direccion',
            'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.fields['fecha_nacimiento'].initial = timezone.now().date()

        self.fields['username'].help_text = "Máximo 20 caracteres."
        self.fields['password1'].help_text = ""



class PerfilEditForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['first_name', 'last_name', 'email', 'pais', 'direccion', 'fecha_nacimiento', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'username' in self.fields:
            self.fields['username'].help_text = "Máximo 150 caracteres."
        
        