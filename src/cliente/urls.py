from cliente import views as cliente_views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import (
    ClienteList,
    ClienteDetail,
    ClienteCreation,
    ClienteUpdate,
    ClienteDelete,
)

urlpatterns = [

    url(r'^listaCliente/$', login_required(ClienteList.as_view()), name='clientelist'),
    url(r'^cliente/(?P<pk>[0-9]{5,10})/$', login_required(ClienteDetail.as_view()), name='clientedetail'),
    url(r'^editarCliente/(?P<pk>[0-9]{5,10})/$', login_required(ClienteUpdate.as_view()), name='clienteupdate'),
    url(r'^nuevoCliente$', login_required(ClienteCreation.as_view()), name='nuevocliente'),
    url(r'^borrarCliente/(?P<pk>\d+)$', login_required(ClienteDelete.as_view()), name='clientedelete'),

]
