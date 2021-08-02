from django.urls import path, include
from .views import SellerListView,OrderDetailTech, SellerProductDetailview, SellerDetailview,MarketDetailview,SellerFilterView,ActionViewSeller

urlpatterns = [
   path('sellers/', SellerListView.as_view(), name='seller'),
   path('filter', SellerFilterView.as_view(), name='filter'),
   path('seller_products/<int:pk>', SellerProductDetailview.as_view(),name='seller_product'),
   path('detail_product', SellerDetailview.as_view(), name="detail_products"),
   path('market_d', MarketDetailview.as_view(), name="market_d"),
   path('order-create/<int:pk>/', OrderDetailTech.as_view(), name="order_create"),
   path('actions3/', ActionViewSeller.as_view(), name="action_view_seller")



]  