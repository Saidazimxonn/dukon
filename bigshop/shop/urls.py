from django.urls import  path, include
from .views import CategoryDetailView, CompanyListView, ProductInfoView
from .views import OrderDetail, ActionViewShop
urlpatterns = [
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('category_detail', ProductInfoView.as_view(), name = 'detail'),
    path('company-list/', CompanyListView.as_view(), name='company'),
    path('order-shop-create/<int:pk>/', OrderDetail.as_view(), name="order_shop_create"),
    path('actions1/', ActionViewShop.as_view(), name="action_view_bazar")

]


