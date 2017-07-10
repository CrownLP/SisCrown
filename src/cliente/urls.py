from cliente import views as cliente_views
from django.conf.urls import url, include

from .views import (
    ClienteList,
    ClienteDetail,
    ClienteCreation,
    ClienteUpdate,
    ClienteDelete,
)

urlpatterns = [

    url(r'^listaCliente/$', ClienteList.as_view(), name='clientelist'),
    url(r'^cliente/(?P<pk>[0-9]{5,10})/$', ClienteDetail.as_view(), name='clientedetail'),
    url(r'^editarCliente/(?P<pk>[0-9]{5,10})/$', ClienteUpdate.as_view(), name='clienteupdate'),
    url(r'^nuevoCliente$', ClienteCreation.as_view(), name='nuevocliente'),
    url(r'^borrarCliente/(?P<pk>\d+)$', ClienteDelete.as_view(), name='clientedelete'),

]
