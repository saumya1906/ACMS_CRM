	
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.Home),
    url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
