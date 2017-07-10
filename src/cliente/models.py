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

    dni = models.CharField(max_length=20,primary_key=True,blank = False,unique = True)
    NACIONALIDADES = (
    ('BOLIVIANA', 'Boliviana',),
    ('EXTRANJERO', 'Extranjero',)
    )
    nacionalidad = models.CharField(max_length=30,blank = False,choices= NACIONALIDADES, default = 'BOLIVIANA')
    direccion = models.CharField(max_length=100,blank=True,unique = False)
    nit = models.CharField(max_length=20,blank = True,unique = False)
    nombre = models.CharField(max_length=60, blank=False,unique = False)
    appaterno = models.CharField(max_length=50,blank=True,unique = False)
    apmaterno = models.CharField(max_length=50,blank=True,unique = False)
    GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
    )
    genero = models.CharField(max_length=30, choices= GENEROS, blank = False, default = 'M')
    correo = models.EmailField(max_length=50,blank=True,unique = False)
    celular = models.IntegerField(null=True, blank=True,unique = False)
    fijo = models.IntegerField(null=True,blank=True,unique = False)
    nacimiento = models.DateTimeField(default = timezone.now)
    vendedor = models.ForeignKey(User,related_name='vendedor', null = True)

    user = models.ForeignKey(User)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.nombre
