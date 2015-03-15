from django.conf.urls import patterns, include, url
from .views import IndexView, AppView
urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^app/$', AppView.as_view(), name='app'),
    url(r'^logout/$', "users.views.log_out", name='logout'),
    url(r'^login/', "users.views.log_in", name="login"),
    url(r'^registrate/', "users.views.registrate", name="registrate"),
    
)
