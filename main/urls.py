
from django.urls import path 
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('event', views.event, name='event'),
    path('education', views.education, name='education'),
    path('about', views.about, name='about'),
    path('health', views.health, name='health'),
    path('development', views.development, name='development'),
]