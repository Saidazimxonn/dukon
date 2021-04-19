from django.shortcuts import render
from django_middleware_global_request.middleware import get_request
from django.views.generic import  ListView, DetailView
from .models import Company, Product
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
# Create your views here.

class CategoryListView(ListView):
    template_name = 'category.html'
    model = Product
    paginate_by = 2
    # context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        
        context['name'] = Product.objects.all()
        company_n = self.request.GET.get('company', None)
        context['products'] = Product.objects.filter(company_id=company_n)
        conpartylist = Product.objects.all().order_by('-id')
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