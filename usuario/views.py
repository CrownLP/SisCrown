from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy
from .models import Perfil
# Las Vistas de la Aplicacion
class PerfilList(ListView):
    model = Perfil

class PerfilDetail(DetailView):
    model = Perfil
