from gestioncliente import views as gestioncliente_views
from django.conf.urls import url, include

from .views import (
    VisitaList,
    VisitaDetail,
    VisitaCreation,
    )

urlpatterns = [
    url(r'^listaVisita$', VisitaList.as_view(), name='visitalist'),
    url(r'^visita/(?P<pk>[0-9]{1,10})/$', VisitaDetail.as_view(), name='visitadetail'),
    url(r'^nuevaVisita$', VisitaCreation.as_view(), name='nuevavisita'),

]
