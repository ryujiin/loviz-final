
from django.conf.urls import  include, url
from views import *

urlpatterns = [
	url(r'^$',OfinaView.as_view() , name='inicio'),
]