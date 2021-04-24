from django.shortcuts import render
from django.views.generic import TemplateView, View
from .helpers import create_ad
from django.shortcuts import redirect, render
from django.urls import reverse
# Create your views here.
class Proba(TemplateView):
    template_name = 'base.html'



class ActinView(View):

    def post(self, request):
        post_request=request.POST
        actions = {
            'create_ad':create_ad,
        }
        actions[self.request.POST.get('action', None)](post_request)
        return redirect('/')