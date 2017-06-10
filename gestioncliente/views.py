from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import json as simplejson
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from gestioncliente.models import Visita, Oportunidad
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import VisitaForm, OportunidadForm
from django.contrib.auth.decorators import login_required
# Las Vistas de la Aplicacion
class VisitaList(ListView):
    model = Visita

class VisitaDetail(DetailView):
    model = Visita



class VisitaCreation(CreateView):
    model = Visita
    success_url = reverse_lazy('gestion:visitalist')
    form_class = VisitaForm

class OportunidadList(ListView):
    model = Oportunidad

class OportunidadDetail(DetailView):
    model = Oportunidad

class OportunidadCreation(CreateView):
    model = Oportunidad
    success_url = reverse_lazy('gestion:oportunidadlist')
    form_class = OportunidadForm
