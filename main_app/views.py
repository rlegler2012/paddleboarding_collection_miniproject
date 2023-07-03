from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"
