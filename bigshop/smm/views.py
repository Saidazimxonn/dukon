from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import SMM
# Create your views here.

class SMMListView(ListView):
    model = SMM
    template_name = 'smm.html'
    context_object_name = "smm_list"


class SMMDetailView(DetailView):
    model = SMM
    template_name = 'smm_detail.html'
    context_object_name = 'smm_det'