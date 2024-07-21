from django.shortcuts import render, redirect
from .models import events_news
from .forms import New_eventForm

# Create your views here.
def home(request):

    events = events_news.objects.all()
    context = { 'events': events,
        'background_image': 'events_news/img/interior-design-yoga-space.jpg'
    }
    return render(request, 'events_news/events_news.html', context)

def create_event(request):
    error = ""
    if request.method == 'POST':
        form = New_eventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_home')
        else:
            error = "Данные были заполнены некорректно"
    else:
        form = New_eventForm()
        return render(request, 'events_news/add_new_event.html',  {'form': form, 'errors': error, 'background_image': 'events_news/img/group-of-people-sitting-in-lotus-position.jpg'})
