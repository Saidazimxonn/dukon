from django.urls import  path, include
from .views import CategoryDetailView, CompanyListView, ProductInfoView

urlpatterns = [
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('category_detail', ProductInfoView.as_view(), name = 'detail'),
    path('company-list/', CompanyListView.as_view(), name='company')

]


