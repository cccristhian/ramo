from django.conf.urls import url
from . import views


#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [

    url(r'^flor/nueva/$', views.Flor_nuevo, name='flor_nuevo'),
    url(r'^ramo/nueva/$', views.ramo_nuevo, name='ramo_nuevo'),
    url(r'^flores/$', views.listar_flores),
    url(r'^$', views.listar_ramos),
    url(r'^flor/(?P<pk>[0-9]+)/$', views.detalle_flor, name='flor'),
    url(r'^ramo/(?P<pk>[0-9]+)/$', views.detalle_ramo, name='ramo'),
    url(r'^flor/(?P<pk>[0-9]+)/edit/$', views.editar_flor, name='editar_flor'),
    url(r'^borrar_flor/(?P<pk>[0-9]+)/$', views.eliminar_flor, name='borrar_flor'),
    url(r'^borrar_ramo/(?P<pk>[0-9]+)/$', views.eliminar_ramo, name='borrar_ramo'),




    ]
