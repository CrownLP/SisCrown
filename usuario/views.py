from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import json as simplejson
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from usuario.models import Agencia

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

def coords_save(request):
    if request.is_ajax():
        form = UbicacionForm(request.POST)
        if form.is_valid():
            pass
        else:
            return HttpResponse(simplejson.dumps({'ok': False, 'msg':'Debes llenar todos los campos'}), mimetype='application/json')
