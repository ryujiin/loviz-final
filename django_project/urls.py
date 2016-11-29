from django.conf.urls import include, url
from django.views.static import serve

import settings

from rest_framework.routers import DefaultRouter


from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    
]
if settings.DEBUG:
    urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
] + urlpatterns