from django.forms import ModelForm
from django import forms
from .models import Cliente
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'dni',
            'nacionalidad',
            'nit',
            'nombre',
            'appaterno',
            'apmaterno',
            'genero',
            'correo',
            'celular',
            'fijo',
            'nacimiento',
            'vendedor',
        ]
        labels = {
            'dni':'Cedula de Identidad',
            'nacionalidad':'Nacionalidad',
            'nit':'Nit',
            'nombre':'Nombres',
            'appaterno':'Apellido Paterno',
            'apmaterno':'Apellido Materno',
            'genero':'Genero',
            'correo':'Correo Electronico',
            'celular':'Telefono Celular',
            'fijo':'Telefono Fijo',
            'nacimiento':'Fecha de Nacimiento',
            'vendedor':'Ejecutivo de Ventas Asignado',
        }
        widgets = {
            'dni': forms.TextInput (attrs={'class':'form-control'}),
            'nacionalidad': forms.RadioSelect (attrs={'class':'form-control'}),
            'nit': forms.TextInput (attrs={'class':'form-control'}),
            'nombre': forms.TextInput (attrs={'class':'form-control'}),
            'appaterno': forms.TextInput (attrs={'class':'form-control'}),
            'apmaterno': forms.TextInput (attrs={'class':'form-control'}),
            'genero': forms.RadioSelect (attrs={'class':'form-control'}),
            'correo': forms.TextInput (attrs={'class':'form-control'}),
            'celular': forms.TextInput (attrs={'class':'form-control'}),
            'fijo': forms.TextInput (attrs={'class':'form-control'}),
            'nacimiento': forms.TextInput (attrs={'class':'form-control'}),
            'vendedor': forms.Select (attrs={'class':'form-control'}),
            }
