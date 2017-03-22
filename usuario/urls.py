from django.conf.urls import url

from .views import (
    PerfilList,
    PerfilDetail
)

urlpatterns = [

    url(r'^$', PerfilList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PerfilDetail.as_view(), name='detail'),
]
