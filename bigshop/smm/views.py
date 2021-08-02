from django.db.models.fields import SmallIntegerField
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import SMM
# Create your views here.
class Indexview(ListView):
    model  = SMM
    context_object_name = 'smm'
    template_name='index_web.html'
    
class SMMListView(ListView):
    model = SMM
    template_name = 'smm.html'
    paginate_by = 1
    context_object_name = "smm_list"
    


class SMMDetailView(DetailView):
    model = SMM
    template_name = 'smm_detail.html'
    context_object_name = 'smm_det'