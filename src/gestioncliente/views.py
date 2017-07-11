from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import json as simplejson
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from gestioncliente.models import Visita, Oportunidad, Seguimiento
from cliente.models import Cliente
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import VisitaForm, OportunidadForm, SeguimientoForm, SeguimientoFormSet
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView
import logging

# Las Vistas de la Aplicacion


class BuscarView (TemplateView):
    template_name = 'gestioncliente/buscar.html'

    def post (self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        print (buscar) #recoje el valor buscado
        #consulta a la base de datos Objeto cliente por dni
        # Cliente.objects.exclude(dni__isnull=True).exclude(dni__exact='').filter(dni__icontains = buscar)


        clientes_dni = Cliente.objects.filter(dni__icontains = buscar).exclude(dni__exact='').exclude(dni__isnull=True)
        # clientes_dni = clientes_dni.objects.exclude(dni__isnull=True)
        # clientes_nombre = Cliente.objects.exclude(nombre__isnull=True).exclude(nombre__exact='').filter(nombre__icontains = buscar)
        # clientes_paterno = Cliente.objects.exclude(appaterno__isnull=True).exclude(appaterno__exact='').filter(appaterno__icontains = buscar)
        # clientes_materno = Cliente.objects.exclude(apmaterno__isnull=True).exclude(apmaterno__exact='').filter(apmaterno__icontains = buscar)
        # # si la busqueda por CI devuelve albun valor:
        if clientes_dni:
            print (clientes_dni)
            print ("Busqueda realizada con su CI")
            return render (request, 'gestioncliente/buscar.html',{'Clientes':clientes_dni})
        elif clientes_nombre:
            print (clientes_nombre)
            print ("Busqueda realizada con su Nombre")
            return render (request, 'gestioncliente/buscar.html',{'Clientes':clientes_nombre})
        elif clientes_paterno:
            print (clientes_paterno)
            print ("Busqueda realizada con su CI")
            return render (request, 'gestioncliente/buscar.html',{'Clientes':clientes_paterno})
        elif clientes_materno:
            print (clientes_materno)
            print ("Busqueda realizada con su CI")
            return render (request, 'gestioncliente/buscar.html',{'Clientes':clientes_materno})

        # else:
        #     clientes_apellido = Cliente.objects.filter(appaterno__contains = buscar)
        #     print (clientes_apellido)
        #     return render (request, 'gestioncliente/buscar.html', {'clientes_apellido':clientes_apellido, 'clientes_apellido':True})
        # print (clientes_dni)
        # return render (request, 'gestioncliente/buscar.html')




class VisitaList(ListView):
    model = Visita


class VisitaDetail(DetailView):
    model = Visita



class VisitaCreation(CreateView):
    model = Visita
    success_url = reverse_lazy('gestion:visitalist')
    form_class = VisitaForm
    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super(VisitaCreation, self).form_valid(form)


class OportunidadList(ListView):
    model = Oportunidad

class OportunidadDetail(DetailView):
    model = Oportunidad

class OportunidadCreation(CreateView):
    model = Oportunidad
    success_url = reverse_lazy('gestion:oportunidadlist')
    form_class = OportunidadForm

class OportunidadUpdate(UpdateView):
    model = Oportunidad
    success_url = '/'
    form_class = OportunidadForm

class OportunidadDelete(DeleteView):
    model = Oportunidad
    success_url = reverse_lazy('oportunidadlist')

class OportunidadSeguimientoCreate(CreateView):
    model = Oportunidad
    form_class = OportunidadForm
    # fields = ['negociacion', 'modelo_interes']
    success_url = reverse_lazy('oportunidadlist')

    def get_context_data(self, **kwargs):
        data = super(OportunidadSeguimientoCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['seguimiento'] = SeguimientoFormSet(self.request.POST)
        else:
            data['seguimiento'] = SeguimientoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        seguimiento = context['seguimiento']
        with transaction.atomic():
            self.object = form.save()

            if seguimiento.is_valid():
                seguimiento.instance = self.object
                seguimiento.save()
        return super(OportunidadSeguimientoCreate, self).form_valid(form)

class OportunidadSeguimientoUpdate(UpdateView):
    model = Oportunidad
    fields = ['negociacion', 'modelo_interes']
    success_url = reverse_lazy('oportunidadlist')

    def get_context_data(self, **kwargs):
        data = super(OportunidadSeguimientoUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['seguimiento'] = SeguimientoFormSet(self.request.POST, instance=self.object)
        else:
            data['seguimiento'] = SeguimientoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        seguimiento = context['seguimiento']
        with transaction.atomic():
            self.object = form.save()

            if seguimiento.is_valid():
                seguimiento.instance = self.object
                seguimiento.save()
        return super(OportunidadSeguimientoUpdate, self).form_valid(form)
