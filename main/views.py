from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User, auth 
from datetime import datetime
from django.conf import settings
import uuid 
from django.urls import reverse 
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect,  csrf_exempt, requires_csrf_token



@requires_csrf_token
def index(request):


    return render(request, 'index.html' )


@requires_csrf_token
def about(request):


    return render(request, 'about.html' )


@requires_csrf_token
def blog(request):


    return render(request, 'blog.html' )


@requires_csrf_token
def contact(request):


    return render(request, 'contact.html' )


@requires_csrf_token
def causes(request):


    return render(request, 'causes.html' )


@requires_csrf_token
def event(request):


    return render(request, 'event.html' )


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


