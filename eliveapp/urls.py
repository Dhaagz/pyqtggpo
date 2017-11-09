from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from eliveapp.views import channels,index,dashboard,auth

urlpatterns = [
    url(r'^login/$', login, name='django.contrib.auth.views.login'),
    url(r'^password_reset/$', password_reset, name="password_reset"),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
    url(r'^logout/$', logout, {'next_page': '/elive/'}),
    url(r'^register/$', auth.register, name='register'),
    url(r'^$', index.index, name='index'),
    url(r'^dashboard/$', dashboard.dashboard, name='dashboard'),
    url(r'^checkpublishurl.*$', channels.check_publish_url, name='check_publish_url'),
    url(r'^(?P<channel_title>\w+)/$', channels.channel, name='channel'),
    url(r'^dashboard/generate_key$', dashboard.generate_key, name='dashboard/generate_key'),
    url(r'^dashboard/set_topic$', dashboard.generate_key, name='dashboard/set_topic'),
]
