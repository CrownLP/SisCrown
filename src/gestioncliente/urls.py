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
    OportunidadSeguimientoUpdate,
    )

urlpatterns = [
    url(r'^buscar/$', login_required(BuscarView.as_view()), name='buscar'),
    url(r'^listaVisita$', login_required(VisitaList.as_view()), name='visitalist'),
    url(r'^visita/(?P<pk>[0-9]{1,10})/$', login_required(VisitaDetail.as_view()), name='visitadetail'),
    url(r'^oportunidad/(?P<pk>[0-9]{1,10})/$', login_required(OportunidadDetail.as_view()), name='oportunidaddetail'),

    url(r'^nuevaVisita$', login_required(VisitaCreation.as_view()), name='nuevavisita'),

    url(r'^nuevaVisitaAn$', login_required(VisitaCreationAn.as_view()), name='nuevavisitaan'),
    url(r'^nuevaOportunidad$', login_required(OportunidadCreation.as_view()), name='nuevaoportunidad'),
    #urls para seguimiento de vendedores
    url(r'^listaOportunidad$', login_required(OportunidadList.as_view()), name='oportunidadlist'),
    url(r'seguimiento/$', login_required(OportunidadSeguimientoCreate.as_view()), name='seguimiento-add'),
    url(r'editarSeguimiento/(?P<pk>[0-9]+)/$', login_required(OportunidadSeguimientoUpdate.as_view()), name='seguimientoupdate'),

    # url(r'profile/(?P<pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),

]
