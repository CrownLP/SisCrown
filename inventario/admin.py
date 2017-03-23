from django.contrib import admin
from .models import Celular, Instancia, Telefono_IP, Linea_IP, Laptop, Monitor
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.
@admin.register (Celular)
class AdminProduct (admin.ModelAdmin):
    list_display = ('imei','marca','modelo','caracteristica')
    list_filter = ('modelo','marca')

@admin.register(Instancia)
class AdminProduct (admin.ModelAdmin):
    list_display = ('numero','operador','plan')
    list_filter = ('operador','plan')

@admin.register(Telefono_IP)
class AdminProduct (admin.ModelAdmin):
    list_display = ('serie','marca','modelo','departamento_adquisicion')
    list_filter = ('marca','modelo')

@admin.register(Linea_IP)
class AdminProduct (admin.ModelAdmin):
    list_display = ('interno','ip')
    list_filter = ('departamento_creacion','ip')

@admin.register(Laptop)
class AdminProduct (admin.ModelAdmin):
    list_display = ('serie','marca','modelo','sistema_operativo')
    list_filter = ('marca','modelo','sistema_operativo')

@admin.register(Monitor)
class AdminProduct (admin.ModelAdmin):
    list_display = ('serie','marca','modelo','display')
    list_filter = ('marca','modelo','display')
