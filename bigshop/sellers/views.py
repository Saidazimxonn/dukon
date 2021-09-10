
from django.core import paginator
from django.db import models
from django.shortcuts import redirect

from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Bazar, Market, Product, Ad_product
from django.views import View
from django.http  import JsonResponse
from django.db.models import Q
from .helpers import order_create


# Create your views here.

    

class SellerListView(ListView):
    model = Market
    model = Bazar
    model = Ad_product
    template_name = 'seller.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(SellerListView, self).get_context_data(**kwargs)
        baza_list = Market.objects.order_by('-id')
        paginator  = Paginator(baza_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        baza_list = file_exams
        # market = self.request.GET.get('market', 'all')
        # bazar = self.request.GET.get('bazar', 'all')
        # if bazar != 'all':
        #     baza_list = baza_list.filter(bazar_id=int(bazar))
        # if market !='all':
        #     baza_list = baza_list.filter(id=int(market))
        context['market_list'] = baza_list
        context['all_market'] = Market.objects.all()
        context['all_bazar'] = Bazar.objects.all()
        context['product_list'] = Ad_product.objects.all()
        return context

class SellerFilterView(View):
    
    def get(self, request):
     
        market_val = request.GET.get('market_val', ' ')
        elements = Market.objects.all().in_bulk()
     
        if market_val !='all':
            elements = Market.objects.filter(Q(info_shop_product__icontains=market_val)|Q(bazar__name__icontains=market_val)|Q(name__icontains=market_val)).in_bulk()
        sellers = list()
        for seller in elements.values():
            seller_temp = dict(seller.__dict__)
            seller_temp['bazar'] = seller.bazar.name
            try:
                seller_temp.__delitem__('_state')
            except:
                pass
            sellers.append(seller_temp)
        data = {
            'sellers':sellers
        }
        return JsonResponse({'data':data})

class ProductList(View):
    
    def get(self, request):
        elements = Product.objects.all().in_bulk()
        products = list()
        for product in elements.values():
            product_temp = dict(product.__dict__)
           
            try:
                product_temp.__delitem__('_state')
            except:
                pass
            products.append(product_temp)
        data = {
            'products':products
        }
        return JsonResponse({'data':data})

class SellerProductDetailview(TemplateView, MultipleObjectMixin):
        model = Product
        
        template_name = 'seller_product.html'
        paginate_by = 5
        def get_context_data(self, **kwargs):
            product_list = Product.objects.filter(market_id=self.kwargs['pk'])
            context = super(SellerProductDetailview, self).get_context_data(object_list = product_list, **kwargs)
       
       
            paginator = Paginator(product_list, self.paginate_by)
            page = self.request.GET.get('page')
            try:
               file = paginator.page(page)
            except PageNotAnInteger:
               file = paginator.page(1)
            except EmptyPage:
                file = paginator.page(paginator.num_pages)

            context['market'] = Product.objects.filter(market_id=self.kwargs['pk']) 
            context['product'] = file
            
         
            return context 


# class SellerDetailview(DetailView):
#     model = Product
#     template_name = 'detail_product.html'
#     context_object_name  = 'detail_products'
class SellerDetailview(View):
    def get(self, request):
        product_id = request.GET.get('m_product_id', None)
        products = Product.objects.select_related('market').filter(id=product_id).in_bulk()
        product_list = list()
        for pro in products.values():
            pro_temp = dict(pro.__dict__)
            pro_temp['market'] = pro.market.name
            try:
                pro_temp.__delitem__('_state')
            except:
                pass
            product_list.append(pro_temp)
        data = {
            'product_list':product_list
        }
        return JsonResponse({'data':data})
        

# class MarketDetailview(DetailView):
#     model = Market
#     template_name = 'market_detail.html'
#     context_object_name = 'market_detail'
class MarketDetailview(View):
    def get(self, request):
        market_info_id = request.GET.get('market_info_ID', None)
        markets = Market.objects.select_related('bazar').filter(id=market_info_id).in_bulk()
        market_list = list()
        for market in  markets.values():
            market_temp = dict(market.__dict__)
            market_temp['bazar'] = market.bazar.name
            try:
                market_temp.__delitem__('_state')
            except:
                pass
            market_list.append(market_temp)
            
        data = {
            'market_list':market_list
        }
        return JsonResponse({'data':data})
    
class NewProductDetailview(View):
    def get(self, request):
        market_info_id = request.GET.get('new_info_ID', None)
        markets = Ad_product.objects.filter(id=market_info_id).in_bulk()
        new_p_list = list()
        for market in  markets.values():
            market_temp = dict(market.__dict__)
            try:
                market_temp.__delitem__('_state')
            except:
                pass
            new_p_list.append(market_temp)
            
        data = {
            'new_p_list':new_p_list
        }
        return JsonResponse({'data':data})
    
       
class OrderDetailTech(DetailView):
    model = Product
    template_name = 'order_seller_det.html'
    context_object_name = 'order_tech'   
    
    
class ActionViewSeller(View):
    
    def post(self, request):
        post_request=request.POST
        actions = {
            'order_create':order_create,
        }
        actions[self.request.POST.get('action3', None)](post_request)
        return redirect('seller')
        
        
class ProductSellersView(View):
    def get(self, request):
      type_id = request.GET.get('type_id', '')
      if type_id =='1':
          product_type = Product.objects.all().in_bulk()
          types_id = list()
          for type in product_type.values():
              type_temp = dict(type.__dict__)
              try:
                  type_temp.__delitem__('_state')
              except:
                  pass
              types_id.append(type_temp)
          data = {
              'types_product':types_id
          }
          return JsonResponse({'data':data})
      if type_id =='2':
          product_type = Market.objects.all().in_bulk()
          types_id = list()
          for type in product_type.values():
              type_temp = dict(type.__dict__)
              try:
                  type_temp.__delitem__('_state')
              except:
                  pass
              types_id.append(type_temp)
          data = {
              'types_product':types_id
          }
          return JsonResponse({'data':data})
         
            
      