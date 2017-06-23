from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import json as simplejson
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from usuario.models import Agencia, Perfil
from .models import Perfil, Agencia
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import AgenciaForm, RegistroForm
#modulos para poder generar el loguin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#from .forms import AgenciaForm

# Las Vistas de la Aplicacion


class RegistroUsuario (CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy ('usuario:PerfilList')



def authentication (request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get ('form-username', None)
        password = request.POST.get ('form-password', None)
        user = authenticate(username=username, password=password)
        loguin (request,user)
    return render(request, 'login.html',{})


class PerfilList(ListView):
    model = Perfil

class AgenciaList(ListView):
    model = Agencia

class PerfilDetail(DetailView):

    model = Perfil

    def get_context_data(self, **kwargs):
        pro = self.kwargs['pk']
        context = super(PerfilDetail, self).get_context_data(**kwargs)
        context["car"] = pro
        return context

# Agencia.objects.filter(codigo="LPZ001")
 # pk = self.kwargs['pk']
 #        context['orderrecords'] = OrderRecords.objects.filter(account_id=pk)

class AgenciaDetail(DetailView):
    model = Agencia



class AgenciaCreation(CreateView):
    model = Agencia
    success_url = reverse_lazy('usuario:PerfilList')
    form_class = AgenciaForm




class AgenciaCreationCordenadas (CreateView):
    model = Agencia
    fields = ('codigo','lat','lng','user')


def coords_save (request):
    if request.method == 'POST':
        lat = request.POST['lat']
        lng = request.POST['lng']

        Agencia.objects.create(
            lat =lat,
            lng = lng
        )

        return HttpResponse('')


##########################################################333


# def coords_save(request):
#     if request.is_ajax():
#         form = UbicacionForm(request.POST)
#         if form.is_valid():
#             pass
#         else:
#             return HttpResponse(simplejson.dumps({'ok': False, 'msg':'Debes llenar todos los campos'}), mimetype='application/json')
