from cliente import views as cliente_views
from django.conf.urls import url, include

from .views import (
    ClienteList,
    ClienteDetail
)

urlpatterns = [

    url(r'^listaCliente/$', ClienteList.as_view(), name='clientelist'),
    url(r'^cliente/(?P<pk>[0-9]{7})/$', ClienteDetail.as_view(), name='clientedetail')
]
