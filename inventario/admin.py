from django.contrib import admin
from .models import Celular, Instancia
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
