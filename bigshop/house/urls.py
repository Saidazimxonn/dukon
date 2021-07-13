from django.urls import path
from .views import HouseDetailView, HouseListView
urlpatterns = [
    path('home', HouseListView.as_view(), name='home'),
    path('home-detail/<int:pk>/', HouseDetailView.as_view(), name="home-detail")
]