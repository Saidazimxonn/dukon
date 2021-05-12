
from django.urls import path
from .views import ClinicListView, ClinicsDetailView, ClinicsDetailViewInfo
urlpatterns = [
    path('clinics', ClinicListView.as_view(), name="clinics"),
    path('clinics-detail/<int:pk>', ClinicsDetailView.as_view(), name='clinic_detail'),
    path('clinics-info/<int:pk>', ClinicsDetailViewInfo.as_view(), name='clinic_info'),
    
]