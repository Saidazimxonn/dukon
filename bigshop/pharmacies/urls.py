from django.urls import path, include
from .views import PharmacyView, PharmDetail, OrderDetail,ActionView

urlpatterns = [
    path('pharm-list/', PharmacyView.as_view(), name="pharm"),
    path('pharm-detail/<int:pk>/', PharmDetail.as_view(), name="pharm_detail"), 
    path('order-create/<int:pk>/', OrderDetail.as_view(), name="order_create"),
    path('actions/', ActionView.as_view(), name="action_view")
]