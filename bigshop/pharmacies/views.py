from .models import Pharmacy, OrderPharm
from django.views.generic import ListView, DetailView, CreateView, TemplateView,View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_middleware_global_request.middleware import get_request
from .helpers import order_create_pharm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.http import JsonResponse

# Create your views here.



class PharmacyView(ListView):
    model  = Pharmacy

    template_name = 'pharmacy.html'
    paginate_by = 5
    context_object_name = 'pharmacies'



class PharmDetail(View):
    def get(self, request):  
        product_info_id = request.GET.get('product_info_ID', None)
        product = Pharmacy.objects.filter(id=product_info_id).in_bulk()
        product_list = list()
        for pro in product.values():
                    pro_temp = dict(pro.__dict__)
                    try:
                        pro_temp.__delitem__('_state')
                    except:
                        pass
                    product_list.append(pro_temp)
        data = {
                    'product_list':product_list
                }
        return JsonResponse({'data':data})
 
class OrderDetail(DetailView):
    model = Pharmacy
    template_name = 'order_det.html'
    context_object_name = 'order_detail'



class ActionViewPharm1(View):
    
    def post(self, request):
        post_request=request.POST
        actions = {
            'order_create_pharm':order_create_pharm,
        }
        actions[self.request.POST.get('action5', None)](post_request)
        return redirect('pharm')
        
    
    
    
    
    
    

