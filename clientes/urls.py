from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'clientes.views.index', name='exibir'),
    url(r'^clientes/(?P<cliente_id>\d+)$', 'clientes.views.exibir', name='exibir'),
    url(r'^clientes/salvar$', 'clientes.views.salvar'),
    url(r'^lista$', 'clientes.views.listaMedia')
)
