from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"

 #adds artist class for mock database data
class Location:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description


locations = [
  Location ("Little Spokane River", "https://assets.change.org/photos/9/lq/sr/HuLQsrEXlyAdApc-1600x900-noPad.jpg?1622402845",
          "Blah"),
  Location ("Heyburn State Park",
          "https://lh3.googleusercontent.com/p/AF1QipOheBfE-Bixtqcbm3zw5N_wif3JiDaAzkiKEb1I=s1360-w1360-h1020", "lake"),
]

class LocationList(TemplateView):
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = locations # this is where we add the key into our context object for the view to use
        return context