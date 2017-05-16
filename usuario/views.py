from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.core.urlresolvers import reverse_lazy


from .models import Perfil, Agencia
#from .forms import AgenciaForm

# Las Vistas de la Aplicacion
class PerfilList(ListView):
    model = Perfil

class PerfilDetail(DetailView):
    model = Perfil

class AgenciaCreation (CreateView):
    model = Agencia
    fields = ('codigo','lat','lng','user')
