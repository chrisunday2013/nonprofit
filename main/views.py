from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User, auth 
from .models import Contact, Testimonial, Volunteer, Events, News_features
from datetime import datetime
from django.conf import settings
import uuid 
from django.urls import reverse 
from django.contrib import messages
from django.views.decorators.csrf import  requires_csrf_token



@requires_csrf_token
def index(request):
    
    n=''
    if  request.method == "POST":
        full_name= request.POST.get('full_name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')   
        contact = Contact(full_name=full_name, email=email, subject=subject, message=message)
        contact.save()
        n='Data Sent Successfully'
        redirect(index)

    if  request.method == "POST":
        full_name= request.POST.get('full_name')
        email= request.POST.get('email')
        reason_for_joining= request.POST.get('reason_for_joining')
        volunteer = Volunteer(full_name=full_name, email=email, reason_for_joining=reason_for_joining)
        volunteer.save()
        n='Data Sent Successfully'
        redirect(index)    

    events=Events.objects.all()
    news_features=News_features.objects.all()
    return render(request, 'index.html', {"events": events, "news_features": news_features})


@requires_csrf_token
def about(request):

   return render(request, 'about.html' )



@requires_csrf_token
def contact(request):
    
    n=''
    if  request.method == "POST":
        full_name= request.POST.get('full_name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')   
        contact = Contact(full_name=full_name, email=email, subject=subject, message=message)
        contact.save()
        n='Data Sent Successfully'
        redirect(index)

    return render(request, 'contact.html'  )



@requires_csrf_token
def event(request):

    events=Events.objects.all()
    return render(request, 'event.html', {"events": events} )



@requires_csrf_token
def education(request):

    news_features=News_features.objects.all()
    return render(request, 'education.html' , {"news_features": news_features})


@requires_csrf_token
def health(request):

    news_features=News_features.objects.all()
    return render(request, 'health.html' , {"news_features": news_features} )


@requires_csrf_token
def donate(request):

   return render(request, 'donate.html' )



@requires_csrf_token
def faq(request):

   return render(request, 'faq.html' )


@requires_csrf_token
def development(request):

    news_features=News_features.objects.all()
    return render(request, 'development.html', {"news_features": news_features} )



