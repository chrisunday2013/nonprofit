
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
    path('faq', views.faq, name='faq'),
    path('do_policy', views.do_policy, name='do_policy'),
    path('p_policy', views.p_policy, name='p_policy'),
    path('partnership', views.partnership, name='partnership'),
    path('part', views.part, name='part'),
    path('terms', views.terms, name='terms'),
    path('cookies', views.cookies, name='cookies'),
    path('cause', views.cause, name='cause'),
    path('grant', views.grant, name='grant'),
    path('employ', views.employ, name='employ'),
    path('development', views.development, name='development'),


     path('paypal-return', views.paypal_return, name='paypal-return'),
    path('paypal-cancel', views.paypal_cancel, name='paypal-cancel'),
    path("confirm_payment/<str:pk>", views.confirm_payment, name="add"),
    path("payment/", views.initiate_payment, name="initiate-payment"),
    path("<str:ref>/", views.verify_payment, name="verify-payment"),
]