from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def blog(request):
    context = {
        'background_image': 'main/img/88.jpg'
    }
    return render(request, 'main/blog.html', context)

def contacts(request):
    context = {
        'background_image': 'main/img/99.jpg'
    }
    return render(request, 'main/contacts.html', context)

def time(request):
    context = {
        'background_image': 'main/img/time.jpg'
    }
    return render(request, 'main/time.html', context)