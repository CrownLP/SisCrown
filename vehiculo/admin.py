from django.contrib import admin
from .models import Marca
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.
@admin.register (Marca)
class AdminProduct (admin.ModelAdmin):
    list_display = ('codigo','nombre')
    list_filter = ('user','fecha_creacion')
