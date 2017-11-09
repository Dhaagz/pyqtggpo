from django.conf.urls import url
from eloboost.views import index,boostme

from . import views

urlpatterns = [
    url(r'^$', index.index, name="index"),
    url(r'^boost-me/$', boostme.boostme, name='boost-me'),
]
