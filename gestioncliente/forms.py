from django.forms import ModelForm
from django import forms
from .models import Visita
from django.contrib.admin.widgets import AdminDateWidget

class VisitaForm (forms.ModelForm):
    class Meta:
        model = Visita

        fields = [
            'dni',
            'tipo_vehiculos',
            'referencia',
            'vendedor',
            'agencia',
        ]
        labels = {
            'dni': 'CI del Cliente',
            'tipo_vehiculos': 'Vehiculo en el que esta interesado',
            'referencia': 'Referencia de Visita a la Agencia',
            'vendedor': 'Ejecutivo de Ventas Asignado',
            'agencia': 'Agencia',
        }

        widgets = {
            'dni': forms.TextInput (attrs={'class':'form-control'}),
            'tipo_vehiculos': forms.RadioSelect (attrs={'class':'radio-custom radio-inline'}),
            'referencia': forms.Select (attrs={'class':'form-control'}),
            'descripcion': forms.Select (attrs={'class':'form-control'}),
            'vendedor': forms.Select (attrs={'class':'form-control'}),
            'agencia': forms.Select (attrs={'class':'form-control'}),
        }
