from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contacts'),
    path('time', views.time, name='time')
]