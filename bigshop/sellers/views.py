from django.shortcuts import render
from django.views.generic import ListView
from .models import Bazar, Market, Product
# Create your views here.


class SellerListView(ListView):
    model = Market
    template_name = 'seller.html'
    context_object_name = 'market_list'
