from django.conf.urls import url,include
from .views import *
from . import views

urlpatterns = [
    url(r'^post/(?P<slug>[-\w]+)/$', get_post, name='post-get'),
]
