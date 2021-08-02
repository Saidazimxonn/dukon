from django.urls import path
from .views import PharmacyView, PharmDetail, OrderDetail,ActionViewPharm1

urlpatterns = [
    path('pharm-list/', PharmacyView.as_view(), name="pharm"),
    path('pharm-detail', PharmDetail.as_view(), name="pharm_detail"), 
    path('order-create-pharm/<int:pk>/', OrderDetail.as_view(), name="order_create_pharm"),
    path('actions5/', ActionViewPharm1.as_view(), name="action_view_pharm")
]