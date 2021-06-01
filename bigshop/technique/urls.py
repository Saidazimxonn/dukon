from django.urls import path, include
from .views import TechniqueListView, TechniqueDetailView,TechniqueInfoView

urlpatterns = [
    path('technique', TechniqueListView.as_view(), name='technique'),
    path('technique-detail', TechniqueDetailView.as_view(), name="technique_det"),
    path('technique-info', TechniqueInfoView.as_view(), name="technique_info"),
    # path('technique/product/detail/<int:pk>/', TechniqueProductDetailView.as_view(), name="tech_product")

]   