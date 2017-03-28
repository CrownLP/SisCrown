from django.conf.urls import url

from .views import (
    #Vistas de Listado
    AccesorioList,
    CelularList,
    CpuList,
    InstanciaList,
    LaptopList,
    Linea_IPList,
    MonitorList,
    Telefono_IPList,
    #Vistas de Detalle
    AccesorioDetail,
    CelularDetail,
    CpuDetail,
    InstanciaDetail,
    LaptopDetail,
    Linea_IPDetail,
    MonitorDetail,
    Telefono_IPDetail,
    #Vistas para Creacion
    InstanciaCreation
)

urlpatterns = [

    url(r'^accesorio/', AccesorioList.as_view(), name='accesoriolist'),
    url(r'^celular/', CelularList.as_view(), name='celularlist'),
    url(r'^cpu/', CpuList.as_view(), name='cpulist'),
    url(r'^instancia/', InstanciaList.as_view(), name='instancialist'),
    url(r'^laptop/', LaptopList.as_view(), name='laptoplist'),
    url(r'^lineaip/', Linea_IPList.as_view(), name='lineaiplist'),
    url(r'^monitor/', MonitorList.as_view(), name='monitorlist'),
    url(r'^telefonoip/', Telefono_IPList.as_view(), name='telefonoiplist'),

    url(r'^nuevaInstancia$', InstanciaCreation.as_view(), name='new'),

    url(r'^item(?P<pk>\d+)$', AccesorioDetail.as_view(), name='accesoriodetail'),
    url(r'^item(?P<pk>\d+)$', CelularDetail.as_view(), name='celulardetail'),
    url(r'^item(?P<pk>\d+)$', CpuDetail.as_view(), name='cpudetail'),
    url(r'^item(?P<pk>\d+)$', InstanciaDetail.as_view(), name='instanciadetail'),
    url(r'^item(?P<pk>\d+)$', LaptopDetail.as_view(), name='laptopdetail'),
    url(r'^item(?P<pk>\d+)$', Linea_IPDetail.as_view(), name='lineaipdetail'),
    url(r'^item(?P<pk>\d+)$', MonitorDetail.as_view(), name='monitordetail'),
    url(r'^item(?P<pk>\d+)$', Telefono_IPDetail.as_view(), name='telefonoipdetail'),

]
