from usuario import views as usuario_views

from django.conf.urls import url, include



from .views import (
    PerfilList,
    PerfilDetail,
    AgenciaList,
    AgenciaDetail,
    #AgenciaForm
    AgenciaCreation,
    coords_save
)

urlpatterns = [

    url(r'^$', PerfilList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PerfilDetail.as_view(), name='detail'),
    url(r'^listaAgencia$', AgenciaList.as_view(), name='AgenciaList'),

    url(r'^agencia/(?P<pk>[A-Z,0-9]{6})/$', AgenciaDetail.as_view(), name='agenciadetail'),

    url(r'^nuevaAgencia$', AgenciaCreation.as_view(), name='new'),
    url(r'^coords/save$', usuario_views.coords_save),
    #url(r'^coords/save$', 'coords_save', name='coords_save'),
]
