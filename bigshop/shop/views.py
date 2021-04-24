from django.shortcuts import render
from django_middleware_global_request.middleware import get_request
from django.views.generic import  ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from .models import Company, Product
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
# Create your views here.

class CategoryDetailView(DetailView, MultipleObjectMixin):
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
   


class ProductDetailView(DetailView):
    model = Product
    template_name = 'mahsulot.html'
    context_object_name = 'category_d'


class CompanyListView(ListView):
    template_name = 'firmact.html'
    model = Company
    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['firms'] =  Company.objects.all()
        context['salom'] = 'Salom'
        return context