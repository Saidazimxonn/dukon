from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_middleware_global_request.middleware import get_request
from django.views.generic.list import MultipleObjectMixin
from django_middleware_global_request.middleware import get_request
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Bazar, Market, Product


# Create your views here.


class SellerListView(ListView):
    model = Market
    model = Bazar
    template_name = 'seller.html'
    context_object_name = 'market_list'

    def get_context_data(self, **kwargs):
        context = super(SellerListView, self).get_context_data(**kwargs)
        baza_list = Market.objects.all()
        market = self.request.GET.get('market', 'all')
        bazar = self.request.GET.get('bazar', 'all')
        if bazar != 'all':
            baza_list = baza_list.filter(bazar_id=int(bazar))
        if market !='all':
            baza_list = baza_list.filter(id=int(market))
        context['market_list'] = baza_list
        context['all_market'] = Market.objects.all()
        context['all_bazar'] = Bazar.objects.all()
        return context


class SellerProductDetailview(DetailView, MultipleObjectMixin):
        model = Product
        
        template_name = 'seller_product.html'
        paginate_by = 3
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


class SellerDetailview(DetailView):
    model = Product
    template_name = 'detail_product.html'
    context_object_name  = 'detail_products'

class MarketDetailview(DetailView):
    model = Market
    template_name = 'market_detail.html'
    context_object_name = 'market_detail'