from django.views.generic import  View, ListView
from .helpers import create_ad
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Reklama
# Create your views here.
class Proba(ListView):
    model = Reklama
    template_name = 'index.html'
    context_object_name = 'ad_post'
    def get_context_data(self, **kwargs):
        context = super(Proba, self).get_context_data(**kwargs)
        baza_list = Reklama.objects.all()
        context['ad_post'] = baza_list
        print(baza_list)
        return context


class ActinView(View):

    def post(self, request):
        post_request=request.POST
        actions = {
            'create_ad':create_ad,
        }
        actions[self.request.POST.get('action', None)](post_request)
        return redirect('/')
