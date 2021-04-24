from django.urls import  path, include
from .views import CategoryDetailView, ProductDetailView, CompanyListView

urlpatterns = [
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('category_detail/<int:pk>/', ProductDetailView.as_view(), name = 'detail'),
    path('company-list/', CompanyListView.as_view(), name='company')

]