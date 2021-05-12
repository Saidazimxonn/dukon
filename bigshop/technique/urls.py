from django.urls import path, include
from .views import TechniqueListView, TechniqueDetailView, TechniqueProductDetailView

urlpatterns = [
    path('technique', TechniqueListView.as_view(), name='technique'),
    path('technique-detail/<int:pk>/', TechniqueDetailView.as_view(), name="technique_det"),
    path('technique/product/detail/<int:pk>/', TechniqueProductDetailView.as_view(), name="tech_product")

]   