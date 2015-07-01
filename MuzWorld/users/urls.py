from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<user_id>[0-9]+)/music/$', views.music, name = 'music'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user, name = 'user'),
    url(r'^(?P<user_id>[0-9]+)/news/$', views.user_news, name = 'user news'),
    url(r'^(?P<user_id>[0-9]+)/groups/$', views.groups, name = 'groups'),
    url(r'^(?P<user_id>[0-9]+)/friends/$', views.friends, name = 'friends'),
]