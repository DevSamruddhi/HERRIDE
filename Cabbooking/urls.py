"""
URL configuration for Cabbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render

# Create your views here.
from django.urls import path
import HERRIDE.views

urlpatterns = [
    path("home/",HERRIDE.views.home,name='home'),
    path('about/',HERRIDE.views.about,name='about'),
    path("contact",HERRIDE.views.contact,name='contact'),
    path("opportunity/",HERRIDE.views.jobs,name='jobs'),
    path("services/",HERRIDE.views.services,name='services'),
    path("registration/",HERRIDE.views.registration,name='registration'),
    path("userlogin/",HERRIDE.views.userlogin,name='ulogin'),
    path("driverlogin/",HERRIDE.views.driverlogin,name='dlogin'),
    path("map2/",HERRIDE.views.map2,name='map2')
]