from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def start(request):
    return HttpResponse("<h1>Это страница start на Django</h1>")

def contacts(request):
    return HttpResponse("<h1>Это  страница contacts на Django</h1>")

def registration(request):
    return HttpResponse("<h1>Это  страница регистрации на Django</h1>")