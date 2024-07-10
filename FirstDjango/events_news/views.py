from django.shortcuts import render
from .models import events_news

# Create your views here.
def home(request):

    events = events_news.objects.all()
    context = { 'events': events,
        'background_image': 'events_news/img/interior-design-yoga-space.jpg'
    }
    return render(request, 'events_news/events_news.html', context)
