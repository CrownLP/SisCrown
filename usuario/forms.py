from django.forms import ModelForm
from django import forms
from .models import Agencia, Perfil
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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


class RegistroForm (UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo Electronico',
        }
        widgets = {
            'username': forms.TextInput (attrs={'class':'form-control'}),
            'first_name': forms.TextInput (attrs={'class':'form-control'}),
            'last_name': forms.TextInput (attrs={'class':'form-control'}),
            'email': forms.TextInput (attrs={'class':'form-control'}),
        }




#mydate = forms.DateField(widget=widgets.AdminDateWidget)

# widgets
#
# TextInput
# Textarea
#SelectDateWidget
#CheckboxSelectMultiple
#RadioSelect
