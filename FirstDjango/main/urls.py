from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('start', views.start),
    path('contacts', views.contacts),
    path('registration', views.registration)
]