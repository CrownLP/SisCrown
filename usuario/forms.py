from django.forms import ModelForm
from django import forms
from .models import Agencia, Perfil
from django.contrib.admin.widgets import AdminDateWidget


class AgenciaForm (forms.ModelForm):
    class Meta:
        model = Agencia

        fields = [
            'codigo',
            'nombre',
            'foto',
            'descripcion',
            'fecha_creacion',
            'ciudad',
        ]
        labels = {
            'codigo': 'Codigo de Agencia',
            'nombre': 'Nombre de la Agencia',
            'foto': 'Foto de la Agencia',
            'descripcion': 'Descripcion',
            'fecha_creacion': 'Fecha de Creacion',
            'ciudad': 'Ciudad'
        }
        widgets = {
            'codigo': forms.TextInput (attrs={'class':'form-control'}),
            'nombre': forms.TextInput (attrs={'class':'form-control'}),
            'foto': forms.Select (attrs={'class':'form-control'}),
            'descripcion': forms.TextInput (attrs={'class':'form-control'}),
            #'fecha_creacion': forms.DateField (widget = forms.SelectDateWidget),
            'ciudad': forms.RadioSelect (attrs={'class':'form-control'}),
        }

#mydate = forms.DateField(widget=widgets.AdminDateWidget)

# widgets
#
# TextInput
# Textarea
#SelectDateWidget
#CheckboxSelectMultiple
#RadioSelect
