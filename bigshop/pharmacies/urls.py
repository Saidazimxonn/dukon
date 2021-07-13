from django.urls import path, include
from .views import PharmacyView, PharmDetail, OrderDetail,ActionViewPharm

urlpatterns = [
    path('pharm-list/', PharmacyView.as_view(), name="pharm"),
    path('pharm-detail', PharmDetail.as_view(), name="pharm_detail"), 
    path('order-create/<int:pk>/', OrderDetail.as_view(), name="order_create"),
    path('actions1/', ActionViewPharm.as_view(), name="action_view_pharm")
]