from django.urls import path
from .views import SMMListView, SMMDetailView
urlpatterns = [
    path('smm', SMMListView.as_view(), name='smm'),
    path('smm-detail/<int:pk>/', SMMDetailView.as_view(), name="smm-detail")
]