from django import forms
from .models import Instancia

class InstanciaForm (forms.ModelForm):
    class Meta:
        model = Instancia

        fields = [
            'numero',
            'sim',
            'operador',
            'plan',
            'departamento_origen',
            'observacion',
        ]
        labels = {
            'numero': 'Numero de Linea Movil',
            'sim': 'Numero de Sim Card',
            'operador': 'Operador',
            'plan': 'Plan de la Linea',
            'departamento_origen': 'Departamento de Alta',
            'observacion': 'Observacion Adicional',
        }
        widgets = {
            'numero': forms.TextInput (attrs={'class':'form-control'}),
            'sim': forms.TextInput (attrs={'class':'form-control'}),
            'operador': forms.Select (attrs={'class':'form-control'}),
            'plan': forms.TextInput (attrs={'class':'form-control'}),
            'departamento_origen': forms.Select (attrs={'class':'form-control'}),
            'observacion': forms.TextInput (attrs={'class':'form-control'}),
        }
