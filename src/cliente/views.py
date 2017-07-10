# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from cliente.models import Cliente
from .forms import ClienteForm

# Las Vistas de la Aplicacion
class ClienteList(ListView):
    model = Cliente

class ClienteDetail(DetailView):
    model = Cliente

class ClienteCreation (CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy ('cliente:clientelist')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClienteCreation, self).form_valid(form)

class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = reverse_lazy('cliente:clientelist')
    form_class = ClienteForm

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente:clientelist')
