from django.contrib import admin
from .models import Categorys, Clinics
# Register your models here.

class CategorysAdmin(admin.ModelAdmin):
    list_display=[
        'name'
    ]
class ClinicsAdmin(admin.ModelAdmin):
    list_display=[
        'name'
    ]
admin.site.register(Categorys, CategorysAdmin)
admin.site.register(Clinics, ClinicsAdmin)