from django.conf.urls import url

from .views import (
    InstanciaList,
    CelularList,
    InstanciaDetail,
    CelularDetail
)

urlpatterns = [

    url(r'^instanciaa/', InstanciaList.as_view(), name='list'),
    url(r'^instancia(?P<pk>\d+)$', InstanciaDetail.as_view(), name='detail'),


]
