from django.contrib import admin
from .models import Categorys, Clinics
# Register your models here.

class CategorysAdmin(admin.ModelAdmin):
    list_display=[
        'name'
    ]
class ClinicsAdmin(admin.ModelAdmin):
    list_display=[
        'name', 'category','info_service', 'phone'
    ]
    list_display_links = [
        'name', 'category','info_service', 'phone'
    ]
    class Meta:
        app_label = 'My APP name'
admin.site.register(Categorys, CategorysAdmin)
admin.site.register(Clinics, ClinicsAdmin)