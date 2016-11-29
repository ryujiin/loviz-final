
from django.conf.urls import  include, url
from views import *
from pedido.views import felicidades

urlpatterns = [
	url(r'^$',HomeView.as_view() , name='index'),
	#url(r'^sitemap\.xml$', 'cmsweb.views.sitemap',name='sitemap'),
	#url(r'^ingresar/$',TiendaView.as_view() , name='ingresar'),
	url(r'^catalogo/',HomeView.as_view() , name='catalogo'),
	url(r'^producto/',HomeView.as_view() , name='producto'),
	url(r'^carro/',HomeView.as_view() , name='carro'),
	url(r'^usuario/perfil/$',HomeView.as_view() , name='carro'),
	url(r'^procesar-compra/',HomeView.as_view() , name='procesar'),
	#url(r'^sp/',TiendaView.as_view() , name='page_static'),
	url(r'^felicidades/$',felicidades , name='felicidades'),
	#url(r'^custom/$',CustomView.as_view(), name='custom'),
]