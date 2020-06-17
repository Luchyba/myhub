from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('main', views.event, name='event'),
    path('main/services', views.community, name='services'),
    path('main/team', views.team, name='team'),
    path('main/camp', views.camp, name='bootcamps'),
    path('main/about', views.about, name='about'),
    path('main/volunteer', views.volunteer, name='volunteer'),
    path('main/incubate', views.incubate, name='incubate'),
    path('main/it4gh', views.it4gh, name='it4gh'),
    path('main/ccoc', views.ccoc, name='ccoc'),
    path('main/contact', views.contact, name='contact'),
]
