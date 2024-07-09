from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'events_news/events_news.html')
