from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User, auth 
from .models import Contact, Testimonial, Volunteer, Events, News_features, Donate,Order, Payment
from datetime import datetime
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import uuid 
from . import forms 
from django.urls import reverse 
from django.contrib import messages
from django.views.decorators.csrf import  requires_csrf_token
from django.urls import reverse 



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
def donate(request):
    
    n=''
    if  request.method == "POST":
        amount= request.POST.get('amount')
        full_name= request.POST.get('full_name')
        email= request.POST.get('email')
        message= request.POST.get('message')   
        payment= request.POST.get('payment')   
        donate = Donate(amount=amount, full_name=full_name, email=email, message=message, payment=payment)
        donate.save()
        n='Data Sent Successfully'
        redirect(index)

    return render(request, 'donate.html' ) 





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
def do_policy(request):

   return render(request, 'do_policy.html' )


@requires_csrf_token
def p_policy(request):

   return render(request, 'p_policy.html' )


@requires_csrf_token
def cookies(request):

   return render(request, 'cookies.html' )


@requires_csrf_token
def partnership(request):

   return render(request, 'partnership.html' )



@requires_csrf_token
def part(request):

   return render(request, 'part.html' )



@requires_csrf_token
def terms(request):

   return render(request, 'terms.html' )


@requires_csrf_token
def cause(request):

   return render(request, 'cause.html' )


@requires_csrf_token
def grant(request):

   return render(request, 'grant.html' )


@requires_csrf_token
def employ(request):

   return render(request, 'employ.html' )




@requires_csrf_token
def development(request):

    news_features=News_features.objects.all()
    return render(request, 'development.html', {"news_features": news_features} )




@requires_csrf_token
def home(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL, 
        'amount': '30.00', 
        'currency_code': 'USD', 
        'item_name': 'Product 1', 
        'invoice': str(uuid.uuid4()), 
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}',
        'cancel_return': f'http://{host}{reverse("paypal-cancel")}',

    }    
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form':form}
    return render(request, 'home.html', context)


@requires_csrf_token
def paypal_return(request):
    messages.success(request, 'You have successfully made a donation payment!')
    return redirect('index')   


@requires_csrf_token
def paypal_cancel(request):
    messages.error(request, 'Your donation payment was cancelled.')
    return redirect('index')


@requires_csrf_token
def confirm_payment(request, pk):
    order = Order.objects.get(id=pk)
    order.completed = True 
    order.save()
    messages.success(request, "Payment made successfully")


@requires_csrf_token
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST": 
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, "make_payment.html", {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else: 
        payment_form = forms.PaymentForm()
    return render(request, 'initiate_payment.html', {'payment_form': payment_form})            


@requires_csrf_token
def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verification Successful')
    else:
        messages.error(request, 'verification Failed') 

    return redirect('/')

    

