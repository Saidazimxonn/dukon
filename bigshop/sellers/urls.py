from django.urls import path, include
from .views import SellerTemplateView

urlpatterns = [
   path('sellers', SellerTemplateView.as_view(), name='seller')

]   