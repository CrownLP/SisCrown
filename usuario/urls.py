from django.conf.urls import url

from .views import (
    PerfilList,
    PerfilDetail,
    #AgenciaForm
    AgenciaCreation
)

urlpatterns = [

    url(r'^$', PerfilList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PerfilDetail.as_view(), name='detail'),
    url(r'^nuevaAgencia$', AgenciaCreation.as_view(), name='new'),
    #url(r'^coords/save$', 'coords_save', name='coords_save'),


]
