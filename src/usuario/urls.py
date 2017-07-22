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
    AgenciaUpdate,
    AgenciaDelete,
    coords_save,
    RegistroUsuario,
    PerfilCreation,
    RegistroCompleto,
    change_password,
    UsuarioList,
    PerfilUpdate,
    PerfilDelete,
)

urlpatterns = [
    url(r'^password/$', change_password, name='change_password'),
    url(r'^registroCompleto', login_required(RegistroCompleto.as_view()), name='registrocompleto'),
    url(r'^login/$', login,{'template_name':'login.html'}, name='login'),
    url(r'^listaAgencia$', login_required(AgenciaList.as_view()), name='AgenciaList'),
    url(r'^listaPerfil$', login_required(PerfilList.as_view()), name='PerfilList'),
    url(r'^editarAgencia/(?P<pk>[A-Z,0-9]{6})/$', login_required(AgenciaUpdate.as_view()), name='agenciaupdate'),
    url(r'^borrarAgencia/(?P<pk>[A-Z,0-9]{6})/$', login_required(AgenciaDelete.as_view()), name='agenciadelete'),
    url(r'^agencia/(?P<pk>[A-Z,0-9]{6})/$', login_required(AgenciaDetail.as_view()), name='agenciadetail'),

    url(r'^nuevaAgencia$', login_required(AgenciaCreation.as_view()), name='nuevaagencia'),
    url(r'^nuevoPerfil$', login_required(PerfilCreation.as_view()), name='nuevoperfil'),
    url(r'^coords/save$', usuario_views.coords_save),

    url(r'^editarPerfil/(?P<pk>[0-9]{2,8})/$', login_required(PerfilUpdate.as_view()), name='perfilupdate'),
    url(r'^borrarPerfil/(?P<pk>[0-9]{2,8})/$', login_required(PerfilDelete.as_view()), name='perfildelete'),
    url(r'^listaUsuario$', login_required(UsuarioList.as_view()), name='usuariolist'),
    url(r'^registrar', RegistroUsuario.as_view(), name='registro'),
    url(r'^perfil/(?P<pk>[0-9]{2,8})/$', PerfilDetail.as_view(), name='perfildetail'),
    #url(r'^coords/save$', 'coords_save', name='coords_save'),
]
