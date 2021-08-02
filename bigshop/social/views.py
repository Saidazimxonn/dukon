from django.shortcuts import render
from .models import Categorya_M, Messanger
from django.views.generic import ListView, DetailView
from django.views import View
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_middleware_global_request.middleware import get_request
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Count
from django.http import JsonResponse


# Create your views here.
class TelegramView(ListView):
    model = Messanger
    template_name = 'teg_messanger.html'
    def get_context_data(self, **kwargs):
        context = super(TelegramView, self).get_context_data(**kwargs)
        context_tg = Messanger.objects.filter(category_id=category_id)
class MessangerListView(ListView):
    model = Categorya_M
    model = Messanger
    template_name = 'messanger.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        cetegory_id = self.request.GET.get('cetegory', 'all')
        context = super(MessangerListView, self).get_context_data(**kwargs)
        clinics_filter = Messanger.objects.all()
        paginator = Paginator(clinics_filter, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['messangers_list'] = file_exams
        context['categorys_m_list'] = Categorya_M.objects.all().annotate(count=Count('categor'))
        return context

# class ClinicsDetailView(View, MultipleObjectMixin):
#     model = Clinics
#     template_name = 'clinics_detail.html'
#     paginate_by = 10
#     def get_context_data(self, **kwargs):
#         produc_list = Clinics.objects.filter(category_id=self.kwargs['pk'])
#         context = super(ClinicsDetailView, self).get_context_data(object_list = produc_list, **kwargs)

#         paginator = Paginator(produc_list, self.paginate_by)
#         page = self.request.GET.get('page')

#         try:
#             file = paginator.page(page)
#         except PageNotAnInteger:
#             file = paginator.page(1)
#         except EmptyPage:
#             file = paginator.page(paginator.num_pages)
#         context['product'] = file
#         context['name'] = Clinics.objects.filter(category_id=self.kwargs['pk'])
#         context['clinics_list'] = Categorys.objects.all().annotate(count=Count('products'))
#         return context



class MessangerDetailView(View):
    paginate_by=1
    def get(self, request):
        category_id = request.GET.get('category_id', None)
        cate = Messanger.objects.select_related('category').filter(category_id=category_id).in_bulk()
        clinics = list()
        for clin in cate.values():
            clin_temp = dict(clin.__dict__)
            clin_temp['category'] = clin.category.name
            try:
                clin_temp.__delitem__('_state')
            except:
                pass
         
            clinics.append(clin_temp)
        data = {
            'clinics':clinics
        }
        return JsonResponse({'data':data})
       
       
 

# class ClinicsDetailViewInfo(DetailView):
#     model = Clinics
#     template_name = 'clinic_info.html'
#     context_object_name = 'clinics_info'

class MessangerDetailViewInfo(View):
    def get(self, request):
        clinic_info_id = request.GET.get('clinic_info_id', None)
        info_c = Messanger.objects.select_related('category').filter(id=clinic_info_id).in_bulk()
        info_list = list()
        for info in info_c.values():
            info_temp = dict(info.__dict__)
            info_temp['category'] = info.category.name
            try:
                info_temp.__delitem__('_state')
            except:
                pass
            info_list.append(info_temp)           
        data = {
            'info_clinic':info_list
        }
        return JsonResponse({'data':data})