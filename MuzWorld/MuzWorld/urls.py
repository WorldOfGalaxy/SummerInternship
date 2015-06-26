from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^user/', include('users.urls')),
<<<<<<< HEAD
	url(r'^registration/', include('registration.urls')),
=======
	url(r'^registration/', include('users.urls')),
>>>>>>> Regina
    url(r'^admin/', include(admin.site.urls)),
]
