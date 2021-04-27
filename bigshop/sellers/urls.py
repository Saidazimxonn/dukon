from django.urls import path, include
from .views import SellerListView, SellerProductDetailview

urlpatterns = [
   path('sellers', SellerListView.as_view(), name='seller'),
   path('seller_products/<int:pk>', SellerProductDetailview.as_view(),name='seller_products')


]   