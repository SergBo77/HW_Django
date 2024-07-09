from django.shortcuts import render
from .models import events_news

# Create your views here.
def home(request):
    events = events_news.objects.all()
    return render(request, 'events_news/events_news.html', {'events': events})
