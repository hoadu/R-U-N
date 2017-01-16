from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add$', views.add, name='add'),
    url(r'(?P<apt_id>\d+)$', views.edit, name='edit'),
    url(r'(?P<apt_id>\d+)/update$', views.update, name='update'),
    url(r'(?P<apt_id>\d+)/delete$', views.delete, name='delete'),
]