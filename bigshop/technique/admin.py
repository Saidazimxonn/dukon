from django.contrib import admin
from .models import Sections, Equipments
# Register your models here.
class SectionsAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'id'
    ]

class EquipmentsAdmin(admin.ModelAdmin):
    list_display =[
        'id','name','company_id'
    ]
    list_filter = [
        'company'
    ]
admin.site.register(Sections, SectionsAdmin)
admin.site.register(Equipments, EquipmentsAdmin)