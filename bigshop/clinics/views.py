from django.shortcuts import render
from .models import Categorys, Clinics
from django.views.generic import ListView,DetailView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_middleware_global_request.middleware import get_request
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Count

# Create your views here.

class ClinicListView(ListView):
    model = Categorys
    model = Clinics
    template_name = 'clinics.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        cetegory_id = self.request.GET.get('cetegory', 'all')
        context = super(ClinicListView, self).get_context_data(**kwargs)
        clinics_filter = Clinics.objects.all()
        paginator = Paginator(clinics_filter, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['clinics_list'] = file_exams
        context['categorys_list'] = Categorys.objects.all().annotate(count=Count('products'))
        return context

class ClinicsDetailView(DetailView, MultipleObjectMixin):
    model = Clinics
    template_name = 'clinics_detail.html'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        produc_list = Clinics.objects.filter(category_id=self.kwargs['pk'])
        context = super(ClinicsDetailView, self).get_context_data(object_list = produc_list, **kwargs)

        paginator = Paginator(produc_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file = paginator.page(page)
        except PageNotAnInteger:
            file = paginator.page(1)
        except EmptyPage:
            file = paginator.page(paginator.num_pages)
        context['product'] = file
        context['name'] = Clinics.objects.filter(category_id=self.kwargs['pk'])
        context['clinics_list'] = Categorys.objects.all().annotate(count=Count('products'))
        return context

class ClinicsDetailViewInfo(DetailView):
    model = Clinics
    template_name = 'clinic_info.html'
    context_object_name = 'clinics_info'