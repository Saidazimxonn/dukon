from .models import Pharmacy, Order
from django.views.generic import ListView, DetailView, CreateView, TemplateView,View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_middleware_global_request.middleware import get_request
from .helpers import order_create
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.



class PharmacyView(ListView):
    model  = Pharmacy
    model = Order
    template_name = 'pharmacy.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PharmacyView, self).get_context_data(**kwargs)
        phrarm_list = Pharmacy.objects.all()
        paginator = Paginator(phrarm_list, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['pharmacies'] = file_exams

        return context


class PharmDetail(DetailView):
    model = Pharmacy
    template_name = 'pharm_det.html'
    context_object_name = 'pharmacy_detail'
class OrderDetail(DetailView):
    model = Pharmacy
    template_name = 'order_det.html'
    context_object_name = 'order_detail'
    
class ActionView(View):
    
    def post(self, request):
        post_request=request.POST
        actions = {
            'order_create':order_create,
        }
        actions[self.request.POST.get('action', None)](post_request)
        return redirect('pharm')
        
    
    
    
    
    
    

