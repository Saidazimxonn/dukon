from django.urls import path, include
from .views import TechniqueListView, TechniqueDetailView,TechniqueInfoView, ActionViewTech, OrderDetailTech

urlpatterns = [
    path('technique', TechniqueListView.as_view(), name='technique'),
    path('technique-detail', TechniqueDetailView.as_view(), name="technique_det"),
    path('technique-info', TechniqueInfoView.as_view(), name="technique_info"),
    path('order-tech-create/<int:pk>/', OrderDetailTech.as_view(), name="order_tech_create"),
    path('actions2/', ActionViewTech.as_view(), name="action_view_tech")

]   