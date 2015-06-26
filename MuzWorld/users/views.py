from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from .models import Comment

def user(request, user_id):
	return HttpResponse("Here will be user %s" % user_id)

def music(request, user_id):
	return HttpResponse("Here will be music of user %s" % user_id)

def groups(request, user_id):
	return HttpResponse("Here will be groups of user %s" % user_id)

def friends(request, user_id):
	return HttpResponse("Here will be friends of user %s" % user_id)

def registration(request):
    return render(request, 'users/register.html')

