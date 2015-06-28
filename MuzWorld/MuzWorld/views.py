from django.http import HttpResponse
from django.shortcuts import render

def registration(request):
    return render(request, 'users/register.html')

def global_news(request):
    return HttpResponse('Here will be global news')

def index(request):
    return HttpResponse('Here will be main')
