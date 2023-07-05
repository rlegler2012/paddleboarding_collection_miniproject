from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('locations/', views.LocationList.as_view(), name="location_list"),
    path('rentals/', views.RentalList.as_view(), name="rental_list")
]