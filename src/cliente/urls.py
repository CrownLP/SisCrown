from cliente import views as cliente_views
from django.conf.urls import url, include

from .views import (
    ClienteList,
    ClienteDetail,
    ClienteCreation
)

urlpatterns = [

    url(r'^listaCliente/$', ClienteList.as_view(), name='clientelist'),
    url(r'^cliente/(?P<pk>[0-9]{7})/$', ClienteDetail.as_view(), name='clientedetail'),
    url(r'^nuevoCliente$', ClienteCreation.as_view(), name='nuevocliente'),

]
