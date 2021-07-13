
from django.urls import path
from .views import MessangerListView, MessangerDetailView, MessangerDetailViewInfo
urlpatterns = [
    
    path('messangers', MessangerListView.as_view(), name="messangers"),
    path('messanger_detail/', MessangerDetailView.as_view(), name='messanger_detail'),
    path('messanger-info', MessangerDetailViewInfo.as_view(), name='messanger_info'),
    
    
]