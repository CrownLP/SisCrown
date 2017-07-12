from gestioncliente import views as gestioncliente_views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from .views import (
    VisitaList,
    VisitaDetail,
    VisitaCreation,
    VisitaCreationAn,
    OportunidadList,
    OportunidadDetail,
    OportunidadCreation,
    BuscarView,
    OportunidadSeguimientoCreate,
    )

urlpatterns = [
    url(r'^buscar/$', BuscarView.as_view(), name='buscar'),
    url(r'^listaVisita$', VisitaList.as_view(), name='visitalist'),
    url(r'^visita/(?P<pk>[0-9]{1,10})/$', VisitaDetail.as_view(), name='visitadetail'),
    url(r'^oportunidad/(?P<pk>[0-9]{1,10})/$', OportunidadDetail.as_view(), name='oportunidaddetail'),
    url(r'^nuevaVisita$', login_required(VisitaCreation.as_view()), name='nuevavisita'),
    url(r'^nuevaVisitaAn$', login_required(VisitaCreationAn.as_view()), name='nuevavisitaan'),
    url(r'^nuevaOportunidad$', OportunidadCreation.as_view(), name='nuevaoportunidad'),
    #urls para seguimiento de vendedores
    url(r'^listaOportunidad$', OportunidadList.as_view(), name='oportunidadlist'),
    url(r'seguimiento/$', OportunidadSeguimientoCreate.as_view(), name='seguimiento-add'),



]
