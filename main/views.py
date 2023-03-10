from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User, auth 
from .models import Contact, Testimonial, Volunteer, Events
from datetime import datetime
from django.conf import settings
import uuid 
from django.urls import reverse 
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect,  csrf_exempt, requires_csrf_token



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
    testimonials=Testimonial.objects.all()
    volunteer=Volunteer.objects.all()

    events=Events.objects.all()
    return render(request, 'index.html', {"events": events})


@requires_csrf_token
def about(request):


    return render(request, 'about.html' )


@requires_csrf_token
def blog(request):


    return render(request, 'blog.html' )



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
def causes(request):


    return render(request, 'causes.html' )


@requires_csrf_token
def event(request):

    events=Events.objects.all()
    return render(request, 'event.html', {"events": events} )


@requires_csrf_token
def economic(request):


    return render(request, 'economic.html' )    


@requires_csrf_token
def service(request):


    return render(request, 'service.html' )


@requires_csrf_token
def education(request):


    return render(request, 'education.html' )


@requires_csrf_token
def health(request):


    return render(request, 'health.html' )


@requires_csrf_token
def volunteer(request):


    return render(request, 'volunteer.html' )


@requires_csrf_token
def donate(request):


    return render(request, 'donate.html' )


@requires_csrf_token
def development(request):


    return render(request, 'development.html' )



@requires_csrf_token
def asia(request):


    return render(request, 'asia.html' )



@requires_csrf_token
def africa(request):


    return render(request, 'africa.html' )


@requires_csrf_token
def america(request):


    return render(request, 'america.html' )


@requires_csrf_token
def latin(request):


    return render(request, 'latin.html' )


@requires_csrf_token
def middle(request):


    return render(request, 'middle.html' )



@requires_csrf_token
def europe(request):


    return render(request, 'europe.html' )



