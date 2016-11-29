from django.conf.urls import include, url
from django.views.static import serve

import settings

from rest_framework.routers import DefaultRouter

from django.contrib import admin
admin.autodiscover()

from catalogo.views import CatalogoViewsets,CategoriaViewsets
from cmsweb.views import *
from carro.views import LineasViewsets,CarroViewsets
from cliente.views import salir,nuevo_usuario,ingresar,DireccionViewsets,ComentarioViewSet,ComentarioImagenViewSet
from pago.views import paypal_paymet,get_stripe_key,definir_pago,stripe_paymet,retorn_paypal,get_pago_contraentrega
from pedido.views import PedidoViewSet,MetodoEnvioViewSet
from ubigeo.views import RegionViewset
from utiles.views import ColorViewsets,TallasViewsets

router = DefaultRouter()
router.register(r'productos', CatalogoViewsets,'productos')
router.register(r'categoria', CategoriaViewsets,'categorias')
router.register(r'cms/paginas', PaginaViewsets,'paginas')
router.register(r'carro/lineas', LineasViewsets,'lineas')
router.register(r'pedidos', PedidoViewSet,'pedidos')
router.register(r'metodos_envio',MetodoEnvioViewSet,'mentodos_envios')
router.register(r'ubigeo',RegionViewset,'ubigeo')
router.register(r'cliente/direcciones',DireccionViewsets,'direcciones')
router.register(r'colores',ColorViewsets,'colores')
router.register(r'tallas',TallasViewsets,'tallas')
router.register(r'comentarios',ComentarioViewSet,'comentarios')
router.register(r'comentarioimgs',ComentarioImagenViewSet,'comentarios_imagenes')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

]
if settings.DEBUG:
    urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
] + urlpatterns