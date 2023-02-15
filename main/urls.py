
from django.urls import path 
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('causes', views.causes, name='causes'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('event', views.event, name='event'),
    path('economic', views.economic, name='economic'),
    path('service', views.service, name='service'),
    path('education', views.education, name='education'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('about', views.about, name='about'),
    path('health', views.health, name='health'),
    path('africa', views.africa, name='africa'),
    path('asia', views.asia, name='asia'),
    path('america', views.america, name='america'),
    path('europe', views.europe, name='europe'),
    path('middle', views.middle, name='middle'),
    path('latin', views.latin, name='latin'),
    path('development', views.development, name='development'),
]