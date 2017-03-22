from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy
from .models import Instancia, Celular
# Las Vistas de la Aplicacion

class InstanciaList(ListView):
    model = Instancia
class CelularList(ListView):
    model = Celular


class InstanciaDetail(DetailView):
    model = Instancia
class CelularDetail(DetailView):
    model = Celular
