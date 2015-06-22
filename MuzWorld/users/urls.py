from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<question_id>[0-9]+)/music/$', views.music, name = 'music'),
    url(r'^(?P<question_id>[0-9]+)/$', views.user, name = 'user'),
    url(r'^$', views.registration, name = "reg"),
]