from django.urls import path, include
from .views import SellerListView

urlpatterns = [
   path('sellers', SellerListView.as_view(), name='seller')

]   