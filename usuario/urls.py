from usuario import views as usuario_views

from django.conf.urls import url, include

from .views import (
    PerfilList,
    PerfilDetail,
    #AgenciaForm
    AgenciaCreation,
    coords_save
)

urlpatterns = [

    url(r'^$', PerfilList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PerfilDetail.as_view(), name='detail'),
    url(r'^nuevaAgencia$', AgenciaCreation.as_view(), name='new'),
    url(r'^coords/save$', usuario_views.coords_save),
    #url(r'^coords/save$', 'coords_save', name='coords_save'),


]
