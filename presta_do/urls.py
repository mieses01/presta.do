from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.customer),
        url(r'^cliente/new/$', views.cliente_new, name='cliente_new'),
    ]
