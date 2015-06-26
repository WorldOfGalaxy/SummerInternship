from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^user/', include('users.urls')),
	url(r'^registration/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
