from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class SellerTemplateView(TemplateView):
    template_name = 'seller.html'

