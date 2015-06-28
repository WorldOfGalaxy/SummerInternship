from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^user/', include('users.urls')),
	url(r'^registration/', 'MuzWorld.views.registration', name = 'registration'),
    url(r'^news/', 'MuzWorld.views.global_news', name = 'global news'),
    url(r'^$', 'MuzWorld.views.index', name = 'index'),
    url(r'^admin/', include(admin.site.urls)),
]
