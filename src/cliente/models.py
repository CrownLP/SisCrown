# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Cliente (models.Model):
    # los campos de un cliente:
    # dni
    # NIT
    # Nombres
    # Apellido Paterno
    # Apellido Materno
    # Correo Electronico
    # Telefono Celular
    # Telefono Fijo
    # Fecha de Nacimiento
    # Nacionalidad
    # NIT

    dni = models.CharField(max_length=20,primary_key=True,blank = False, help_text="Documento Nacinal de Identidad",unique = True)
    NACIONALIDADES = (
    ('BOLIVIANA', 'Boliviana',),
    ('EXTRANJERO', 'Extranjero',)
    )
    nacionalidad = models.CharField(max_length=30,blank = False,choices= NACIONALIDADES)
    nit = models.CharField(max_length=20,blank = True, help_text="NIT",unique = False)
    nombre = models.CharField(max_length=60, blank=False,help_text="Nombres",unique = False)
    appaterno = models.CharField(max_length=50,blank=True,help_text="Apellido Parterno",unique = False)
    apmaterno = models.CharField(max_length=50,blank=True,help_text="Apellido Materno",unique = False)
    GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
    )
    genero = models.CharField(max_length=30, choices= GENEROS)
    correo = models.CharField(max_length=50,blank=True,help_text="Correo Electronico",unique = False)
    celular = models.IntegerField(null=True, blank=True,help_text="Telefono Fijo",unique = False)
    fijo = models.IntegerField(null=True,blank=True,help_text="Telefono Celular",unique = False)
    nacimiento = models.DateTimeField(default = timezone.now)

    user = models.ForeignKey(User)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.nombre
