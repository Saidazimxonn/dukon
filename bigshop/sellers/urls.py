from django.urls import path, include
from .views import SellerListView, SellerProductDetailview, SellerDetailview,MarketDetailview

urlpatterns = [
   path('sellers', SellerListView.as_view(), name='seller'),
   path('seller_products/<int:pk>', SellerProductDetailview.as_view(),name='seller_product'),
   path('detail_seller/<int:pk>', SellerDetailview.as_view(), name="detail_product"),
   path('market_detail/<int:pk>', MarketDetailview.as_view(), name="market_d"),


]   