
from django.urls import path
from .views import MessangerListView, MessangerDetailView, MessangerDetailViewInfo
urlpatterns = [
    
    path('telegram', MessangerListView.as_view(), name="telegram"),
    path('telegram_detail/', MessangerDetailView.as_view(), name='telegram_detail'),
    path('telegram-info', MessangerDetailViewInfo.as_view(), name='telegram_info'),
    
    
]