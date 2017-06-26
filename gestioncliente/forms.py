from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import Visita, Oportunidad, Seguimiento
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

class OportunidadForm (forms.ModelForm):
    class Meta:
        model = Oportunidad

        fields = [
            'dni',
            'negociacion',
            'modelo_actual',
            'modelo_interes',
            'tipo_venta',
            'estado',
            'vendedor',
            'agencia',
        ]
        labels = {
            'dni': 'Cliente',
            'negociacion': 'Resumen Negociacion Inicial con el Cliente',
            'modelo_actual': 'Modelo actual del vehiculo del cliente',
            'modelo_interes': 'Modelo en el que esta interesado el cliente',
            'tipo_venta': 'Tipo de Venta',
            'estado': 'Estado',
            'vendedor': 'Ejecutivo de Ventas',
            'agencia': 'Agencia',
        }

        widgets = {
            'negociacion': forms.Textarea (attrs={'class':'form-control'}),
            'dni': forms.Select (attrs={'class':'form-control'}),
            'modelo_actual': forms.TextInput (attrs={'class':'form-control'}),
            'modelo_interes': forms.TextInput (attrs={'class':'form-control'}),
            'tipo_venta': forms.Select (attrs={'class':'form-control'}),
            'estado': forms.Select (attrs={'class':'form-control'}),
            'vendedor': forms.Select (attrs={'class':'form-control'}),
            'agencia': forms.Select (attrs={'class':'form-control'}),
        }


class SeguimientoForm(ModelForm):
    class Meta:
        model = Seguimiento
        fields = [
            'observacion',
            'siguiente_interaccion',
            'tipo_interaccion',
            'interaccion',
            'fecha_creacion',
            'usuario',
        ]
        labels = {
            'observacion':'Negociacion',
            'siguiente_interaccion': 'Fecha siguiente interaccion',
            'tipo_interaccion': '',
            'interaccion': 'Tipo de interaccion',
            'fecha_creacion': 'Fecha de Creacion',
            'usuario': 'Ejecutivo de Ventas',
        }
        widgets = {
            'observacion':forms.Textarea (attrs={'class':'form-control'}),
            'siguiente_interaccion': forms.TextInput (attrs={'class':'form-control'}),
            'tipo_interaccion':forms.RadioSelect (attrs={'class':'radio-custom radio-inline'}),
            'interaccion':forms.Select (attrs={'class':'form-control'}),
            'fecha_creacion': forms.TextInput (attrs={'class':'form-control'}),
            'usuario':forms.Select (attrs={'class':'form-control'}),
        }


SeguimientoFormSet = inlineformset_factory(Oportunidad, Seguimiento,
                                            form=SeguimientoForm, extra=1)
