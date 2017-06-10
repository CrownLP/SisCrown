from gestioncliente import views as gestioncliente_views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from .views import (
    VisitaList,
    VisitaDetail,
    VisitaCreation,
    OportunidadList,
    OportunidadDetail,
    OportunidadCreation,
    )

urlpatterns = [
    url(r'^listaVisita$', VisitaList.as_view(), name='visitalist'),
    url(r'^listaOportunidad$', OportunidadList.as_view(), name='oportunidadlist'),
    url(r'^visita/(?P<pk>[0-9]{1,10})/$', VisitaDetail.as_view(), name='visitadetail'),
    url(r'^oportunidad/(?P<pk>[0-9]{1,10})/$', OportunidadDetail.as_view(), name='oportunidaddetail'),
    url(r'^nuevaVisita$', login_required(VisitaCreation.as_view()), name='nuevavisita'),
    url(r'^nuevaOportunidad$', OportunidadCreation.as_view(), name='nuevaoportunidad'),

]
