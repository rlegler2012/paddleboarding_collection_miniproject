# at top of file
from typing import Any, Dict
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render
# import models
from .models import Location
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class LocationCreate(CreateView):
    model = Location
    fields = ['name', 'img', 'description']
    template_name = "location_create.html"
    success_url = '/locations/'

class LocationList(TemplateView):
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # This is essentially a query built into Django that's saying SELECT * FROM main_app_artist
        # self.request.GET is a dictionary just like in express we have req.query
        # print(self.request.GET)
        name = self.request.GET.get('name')
        if name != None:
            # This is essentially a regex matcher that's built in for us. It's searching for anything where the name of the artist contains (at any point) this name if there is a query
            context["locations"] = Location.objects.filter(name__icontains=name)
        else:
            context["locations"] = Location.objects.all()
        return context
    
class LocationDetail(DetailView):
    model = Location
    template_name = "location_detail.html"

class LocationUpdate(UpdateView):
    model = Location
    fields = ['name', 'img', 'description']
    template_name = "location_update.html"
    success_url = '/locations/'

class LocationDelete(DeleteView):
    model = Location
    template_name = "location_delete_confirmation.html"
    success_url = '/locations/'




# locations = [
#   Location ("Little Spokane River", "https://assets.change.org/photos/9/lq/sr/HuLQsrEXlyAdApc-1600x900-noPad.jpg?1622402845",
#           "Blah"),
#   Location ("Heyburn State Park",
#           "https://lh3.googleusercontent.com/p/AF1QipOheBfE-Bixtqcbm3zw5N_wif3JiDaAzkiKEb1I=s1360-w1360-h1020", "lake"),
# ]