from django.shortcuts import render
from django.views.generic import  ListView, TemplateView, DetailView
from django_middleware_global_request.middleware import get_request
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Count
from .models import Sections, Equipments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
class TechniqueListView(ListView):
    model = Equipments
    model = Sections
    template_name = 'techniqu.html'
    paginate_by = 9
 
    def get_context_data(self, **kwargs):
        context = super(TechniqueListView, self).get_context_data(**kwargs)
        section_filter = Equipments.objects.all()
        paginator = Paginator(section_filter, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['techniques_list'] = file_exams
        context['sections_list'] =  Sections.objects.all().annotate(count=Count('products'))

        return context

class TechniqueDetailView(DetailView, MultipleObjectMixin):

    model = Equipments
    template_name = 'tech_detail.html'
    paginate_by = 2
  

    def get_context_data(self, **kwargs):
        produc_list = Equipments.objects.filter(company_id = self.kwargs['pk'])
        context = super(TechniqueDetailView, self).get_context_data(object_list = produc_list, **kwargs)
       
        paginator = Paginator(produc_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            file = paginator.page(page)
        except PageNotAnInteger:
            file = paginator.page(1)
        except EmptyPage:
            file = paginator.page(paginator.num_pages)
        context['name'] = Equipments.objects.filter(company_id=self.kwargs['pk'])
        context['product'] = file
        context['sections_list'] = Sections.objects.all().annotate(count=Count('products'))
        return context

class TechniqueProductDetailView(DetailView):
    model = Equipments
    template_name = "tech_mahsulot.html"
    context_object_name = "tech_products"

# class SectionsTmplateView(ListView):
#     model = Sections
#     template_name = 'techniqu.html'
#     context_object_name = 'sections_list'

