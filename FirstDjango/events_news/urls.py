from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='events_home'),
    path('create_event', views.create_event, name='add_event')
]