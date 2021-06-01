
from django.urls import path
from .views import ClinicListView, ClinicsDetailView, ClinicsDetailViewInfo
urlpatterns = [
    
    path('clinics', ClinicListView.as_view(), name="clinics"),
    path('clinics/', ClinicsDetailView.as_view(), name='clinic_detail'),
    path('clinics-info', ClinicsDetailViewInfo.as_view(), name='clinic_info'),
    
    
]