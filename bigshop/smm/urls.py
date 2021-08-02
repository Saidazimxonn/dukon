from django.urls import path
from .views import SMMListView, SMMDetailView, Indexview
urlpatterns = [
    path('ind', Indexview.as_view(), name='index'),
    path('smm', SMMListView.as_view(), name='smm'),
    path('smm-detail/<int:pk>/', SMMDetailView.as_view(), name="smm-detail")
]