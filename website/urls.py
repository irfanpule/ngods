from django.conf.urls import url

from .views import index, show_ods, save_ods, download


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^show/$', show_ods, name='show_ods'),
    url(r'^save/$', save_ods, name='save_ods'),
    url(r'^download/$', download, name='download'),
]