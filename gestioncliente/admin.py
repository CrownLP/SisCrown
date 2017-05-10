from django.contrib import admin
from .models import Visita
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.
@admin.register (Visita)
class AdminProduct (admin.ModelAdmin):
    list_display = ('numero','sim')
    list_filter = ('numero','sim')
