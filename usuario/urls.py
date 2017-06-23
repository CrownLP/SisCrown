from usuario import views as usuario_views
from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

from .views import (
    PerfilList,
    PerfilDetail,
    AgenciaList,
    AgenciaDetail,
    #AgenciaForm
    AgenciaCreation,
    coords_save,
    RegistroUsuario
)

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name='registro'),
    url(r'^login/$', login,{'template_name':'login.html'}, name='login'),
    url(r'^listaAgencia$', AgenciaList.as_view(), name='AgenciaList'),
    url(r'^listaPerfil$', PerfilList.as_view(), name='PerfilList'),
    url(r'^agencia/(?P<pk>[A-Z,0-9]{6})/$', AgenciaDetail.as_view(), name='agenciadetail'),
    url(r'^perfil/(?P<pk>[0-9]{2,8})/$', PerfilDetail.as_view(), name='perfildetail'),
    url(r'^nuevaAgencia$', AgenciaCreation.as_view(), name='nuevaagencia'),
    url(r'^coords/save$', usuario_views.coords_save),
    #url(r'^coords/save$', 'coords_save', name='coords_save'),
]
