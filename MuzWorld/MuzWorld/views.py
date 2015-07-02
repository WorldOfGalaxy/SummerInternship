from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def registration(request):		
    return render(request, 'register.html')

def global_news(request):
    return HttpResponse('Here will be global news')

def index(request):
    return render_to_response('index.html')