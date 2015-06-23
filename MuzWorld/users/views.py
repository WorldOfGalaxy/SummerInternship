from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from .models import Comment

def user(request, question_id):
	return HttpResponse("Here will be user %s" % question_id)

def music(request, question_id):
	return HttpResponse("Here will be music of user %s" % question_id)

def registration(request):
    return render(request, 'users/register.html')