from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.shortcuts import render, render_to_response
from .models import Musician, Audio, Comment
from django.contrib.auth.models import User

def user(request, user_id):
	return render_to_response('home.html',{'user': Musician.objects.get(id = user_id), 'audios': Audio.objects.filter(audio_owner_id = user_id), })

def music(request, user_id):
	return HttpResponse("Here will be music of user %s" % user_id)

def groups(request, user_id):
	return HttpResponse("Here will be groups of user %s" % user_id)

def friends(request, user_id):
	return HttpResponse("Here will be friends of user %s" % user_id)

def user_news(request, user_id):
    return HttpResponse("Here will be news of user %s" % user_id)
