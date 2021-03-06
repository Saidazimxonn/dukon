from django.shortcuts import redirect
from django.views.generic import  ListView, DetailView
from django.db.models import Count
from .models import Sections, Equipments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.http import JsonResponse
from .helpers import order_create

# Create your views here.

class TechniqueListView(ListView):
    model = Equipments
    model = Sections
    template_name = 'techniqu.html'
    paginate_by = 5
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
        # cate = Equipments.objects.select_related('company').filter(company_id=category_ID).in_bulk()
        # techniqus = list()
        # for tech in more_posts.values():
        #     tech_temp = dict(tech.__dict__)
        #     tech_temp['company'] = tech.company.name
        #     try:
        #         tech_temp.__delitem__('_state')
        #     except:
        #         pass
        #     techniqus.append(tech_temp)  

        
class TechniqueDetailView(View):
    def get(self, request):
        category_ID = request.GET.get('category_ID', None)
        cate = Equipments.objects.select_related('company').filter(company_id=category_ID).in_bulk()
        techniqus = list()
        for tech in cate.values():
            tech_temp = dict(tech.__dict__)
            tech_temp['company'] = tech.company.name
            try:
                tech_temp.__delitem__('_state')
            except:
                pass
            techniqus.append(tech_temp)
        data={
            'techniqus':techniqus
        }
        return JsonResponse({'data':data})
    
    # @staticmethod
    # def get(request, *args, **kwargs):
    #     last_post_id = request.GET.get('lastPostID', 2)
    #     category_ID = request.GET.get('category_ID', None)
    #     print(last_post_id, '-------------------------------------------------------------------------')
        
    #     more_posts = Equipments.objects.select_related('company').order_by('id').filter(pk__gt=int(last_post_id), company__id=category_ID)\
    #         .values('id', 'name', 'new_price', 'old_price', 'new', 'sale', 'info_text', 'tg_link', 'ins_link', 'company')
    #     if not more_posts:
    #         return JsonResponse({'data':False})
    #     data = []
    #     obj = dict()
    #     for post in more_posts:
    #         obj = {
    #             'id':post['id'],
    #             'name':post['name'],
    #             'new_price':post['new_price'],
    #             'old_price':post['old_price'],
    #             'new':post['new'],
    #             'sale':post['sale'],
    #             'info_text':post['info_text'],
    #             'tg_link':post['tg_link'],
    #             'ins_link':post['ins_link'],
                
    #             'company':post['company'], }
    #         data.append(obj)
    #     data[-1]['last_post']=True
    #     return JsonResponse({'data':data})
    
    
class TechniqueInfoView(View):
  def get(self, request):  
        product_info_id = request.GET.get('product_info_ID', None)
        product = Equipments.objects.select_related('company').filter(id=product_info_id).in_bulk()
        product_list = list()
        for pro in product.values():
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
 

# class TechniqueDetailView(TemplateView, MultipleObjectMixin):
    
#     template_name = 'tech_detail.html'
#     paginate_by = 2
  

#     def get_context_data(self, **kwargs):
#         produc_list = Equipments.objects.all().filter(company_id = self.kwargs['pk'])
#         context = super(TechniqueDetailView, self).get_context_data(object_list = produc_list, **kwargs)
       
#         paginator = Paginator(produc_list, self.paginate_by)
#         page = self.request.GET.get('page')
#         try:
#             file = paginator.page(page)
#         except PageNotAnInteger:
#             file = paginator.page(1)
#         except EmptyPage:
#             file = paginator.page(paginator.num_pages)
#         # context['name'] = Equipments.objects.filter(company_id=self.kwargs['pk'])
#         context['product'] = file
#         context['sections_list'] = Sections.objects.all().annotate(count=Count('products'))
#         return context

# class TechniqueProductDetailView(DetailView):
#     model = Equipments
#     template_name = "tech_mahsulot.html"
#     context_object_name = "tech_products"

# class SectionsTmplateView(ListView):
#     model = Sections
#     template_name = 'techniqu.html'
#     context_object_name = 'sections_list'

class OrderDetailTech(DetailView):
    model = Equipments
    template_name = 'order_tech.html'
    context_object_name = 'order_tech'


    
class ActionViewTech(View):
    
    def post(self, request):
        post_request=request.POST
        actions = {
            'order_create':order_create,
        }
        actions[self.request.POST.get('action2', None)](post_request)
        return redirect('technique')
        