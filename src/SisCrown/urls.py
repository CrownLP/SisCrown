"""SisCrown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete




urlpatterns = [
    #la URL del sitio de administracion
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^$', login,{'template_name':'index.html'}, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', login,{'template_name':'login.html'}, name='login'),
    url(r'^inventario/', include('inventario.urls', namespace='inventario')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
    url(r'^cliente/', include('cliente.urls', namespace='cliente')),
    url(r'^gestion/', include('gestioncliente.urls', namespace='gestion')),
#urls para el reset de password
    url(r'^reset/password_reset', password_reset, {'template_name':'registration/password_reset_form.html',
    'email_template_name':'registration/password_reset_email.html'}, name = 'password_reset'),
    url(r'^reset/envio', password_reset_done, {'template_name':'registration/password_reset_done.html'}, name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name':'registration/password_reset_confirm.html'}, name = 'password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name':'registration/password_reset_complete.html'}, name = 'password_reset_complete'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
