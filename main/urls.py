
from django.urls import path 
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('causes', views.causes, name='causes'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('event', views.event, name='event'),
    path('service', views.service, name='service'),
    path('education', views.education, name='education'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('about', views.about, name='about'),
    path('health', views.health, name='health'),
    path('development', views.development, name='development'),
]