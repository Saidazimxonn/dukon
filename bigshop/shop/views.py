from django.shortcuts import render
from django_middleware_global_request.middleware import get_request
from django.views.generic import  ListView, TemplateView, DetailView
from django.views.generic.list import MultipleObjectMixin
from .models import Company, Product
from django.views import View
from django.http import JsonResponse
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
# Create your views here.

class CategoryDetailView(TemplateView, MultipleObjectMixin):
    template_name = 'category.html'
    model = Product
    paginate_by = 15
    # context_object_name = 'products'
    def get_context_data(self, **kwargs):
        conpartylist = Product.objects.filter(company_id=self.kwargs['pk'])
        context = super(CategoryDetailView, self).get_context_data(object_list=conpartylist, **kwargs)
        
        context['name'] = Product.objects.filter(company_id=self.kwargs['pk'])
        # company_n = self.request.GET.get('company', None)
        paginator = Paginator(conpartylist, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
       
        context['products'] = file_exams

        return context
   


# class ProductDetailView(getFarmInfoElement):
#     model = Product
#     template_name = 'mahsulot.html'
#     context_object_name = 'category_d'
class ProductInfoView(View):
    def get(self, request):
        product_id = request.GET.get('product_id', None)
        farm_product = Product.objects.select_related('company').filter(id=product_id).in_bulk()
        product_list = list()
        for pro in farm_product.values():
            pro_temp = dict(pro.__dict__)
            pro_temp['company'] = pro.company.name
            try:
                pro_temp.__delitem__('_state')
            except:
                pass
            product_list.append(pro_temp)
        data = {
            'product_list':product_list
        }
        return JsonResponse({'data':data})
class CompanyListView(ListView):
    template_name = 'firmact.html'
    model = Company
    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['firms'] =  Company.objects.all()
        context['salom'] = 'Salom'
        return context