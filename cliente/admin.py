# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Cliente
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.
@admin.register (Cliente)
class AdminProduct (admin.ModelAdmin):
    list_display = ('dni','nit','appaterno','apmaterno')
    list_filter = ('genero','nacionalidad')
