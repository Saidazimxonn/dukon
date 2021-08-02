from django.contrib import admin
from .models import Sections, Equipments, Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'name','id'
    ]
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
admin.site.register(Order, OrderAdmin)
