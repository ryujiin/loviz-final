from django.conf.urls import include, url
from django.views.static import serve

import settings

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from django.contrib.sitemaps.views import sitemap
from catalogo.sitemap import *



from django.contrib import admin
admin.autodiscover()

from catalogo.views import CatalogoViewsets,CategoriaViewsets,ListaProductosViewsets,ProductoCalificacionPromedioViewsets
from cmsweb.views import *
from carro.views import LineasViewsets,CarroViewsets
from cliente.views import salir,nuevo_usuario,ingresar,DireccionViewsets,ClienteViewSet,SuscritoViewset
from comentario.views import ComentarioViewSet,ComentarioImagenViewSet
from pago.views import paypal_paymet,get_stripe_key,definir_pago,stripe_paymet,retorn_paypal,get_pago_contraentrega
from pedido.views import PedidoViewSet,MetodoEnvioViewSet,MetodoPagoViewSet,PedidoViewsApi
from ubigeo.views import RegionViewset
from utiles.views import ColorViewsets,TallasViewsets

router = DefaultRouter()
router.register(r'productos', CatalogoViewsets,'productos')
#router.register(r'lista_productos', ListaProductosViewsets,'lista_productos')
router.register(r'categoria', CategoriaViewsets,'categorias')
router.register(r'carro/lineas', LineasViewsets,'lineas')
router.register(r'pedidos', PedidoViewSet,'pedidos')
router.register(r'cliente/direcciones',DireccionViewsets,'direcciones')
router.register(r'ubigeo',RegionViewset,'ubigeo')
router.register(r'metodos_envio',MetodoEnvioViewSet,'mentodos_envios')
router.register(r'metodos_pago',MetodoPagoViewSet,'mentodos_pago')
router.register(r'producto/comentario_promedio',ProductoCalificacionPromedioViewsets,'comentario_promedio')
router.register(r'comentarios',ComentarioViewSet,'comentarios')
router.register(r'comentarioimgs',ComentarioImagenViewSet,'comentarios_imagenes')

router.register(r'cms/paginas', PaginaViewsets,'paginas')
router.register(r'cliente/cliente',ClienteViewSet,'cliente')
router.register(r'cliente/suscrito',SuscritoViewset,'suscritos')
router.register(r'colores',ColorViewsets,'colores')
router.register(r'tallas',TallasViewsets,'tallas')
#Loviz 2.0
router.register(r'cms/hero_home',HeroHomeViewsets,'Hero Home')



sitemaps ={
    'categoria': CategoriaSitemap,
    'productos':ProductoSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/carro/', include('carro.urls')),
    url(r'^api/pedido/actual/',PedidoViewsApi.as_view()),

    #Usauario 
    url(r'^api/user/', include('cliente.urls')),        
    url(r'^ajax/crear/', nuevo_usuario, name='nuevo_usuario'),    
    url(r'^salir/$',salir,name='salir'),
    url(r'^login/$',ingresar,name='salir'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    #Login
    url('', include('social.apps.django_app.urls', namespace='social')),
    #pagos
    url(r'^pago_contraentrega/',get_pago_contraentrega,name='pago_contraentrega'),    
    url(r'^definir_pago/',definir_pago,name='definir_pago'),    
    url(r'^retorno_paypal/',retorn_paypal,name='retorn_paypal'),    
    url(r'^pago/stripe/$',stripe_paymet,name='pago_stripe'),
    url(r'^get_stripe_key/$',get_stripe_key,name='get_key'),    
    url(r'^pago/paypal/', paypal_paymet,name = 'pago_paypal'),    
    url(r'^hardcode/get/paypal/', include('paypal.standard.ipn.urls')),
    #Oficina
    url(r'^oficina/',include('oficina.urls')),
    #Web
    url(r'^',include('cmsweb.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap')
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^debug/', include(debug_toolbar.urls)),
] + urlpatterns