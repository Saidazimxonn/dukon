from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import House
# Create your views here.

class HouseListView(ListView):
    model = House
    template_name = 'home.html'
    context_object_name = "home_list"


class HouseDetailView(DetailView):
    model = House
    template_name = 'det_home.html'
    context_object_name = 'home_det'