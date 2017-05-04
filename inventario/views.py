from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Instancia, Celular, Accesorio, CPU, Laptop, Linea_IP, Telefono_IP, Monitor
from .forms import InstanciaForm

# Las Vistas de Lsiatdo


class AccesorioList(ListView):
    model = Accesorio
class CelularList(ListView):
    model = Celular
class CpuList(ListView):
    model = CPU
class InstanciaList(ListView):
    model = Instancia
class LaptopList(ListView):
    model = Laptop
class Linea_IPList(ListView):
    model = Linea_IP
class MonitorList(ListView):
    model = Monitor
class Telefono_IPList(ListView):
    model = Telefono_IP




class AccesorioDetail(DetailView):
    model = Accesorio
class CelularDetail(DetailView):
    model = Celular
class CpuDetail(DetailView):
    model = CPU
class InstanciaDetail(DetailView):
    model = Instancia
class LaptopDetail(DetailView):
    model = Laptop
class Linea_IPDetail(DetailView):
    model = Linea_IP
class MonitorDetail(DetailView):
    model = Monitor
class Telefono_IPDetail(DetailView):
    model = Telefono_IP

#VISTAS PARA CREAR UNIDADES

class InstanciaCreation(CreateView):
    model = Instancia
    success_url = reverse_lazy('inventario:instancialist')
    form_class = InstanciaForm
    #fields = ['numero', 'sim', 'operador', 'plan', 'departamento_origen']
