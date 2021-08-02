from django.contrib import admin
from .models import Pharmacy, OrderPharm
# Register your models here.


class OrderPharmAdmin(admin.ModelAdmin):
    list_display=(
        'id','product_name', 'name', 'phone' , 'count_product', 'province'
    )
   
    list_display_links=(
        'product_name', 'name', 'phone' , 'count_product', 'province'
    )
 
   

class PharmacyAdmin(admin.ModelAdmin):
    list_display=(
        'id','name', 'pharmacy_info'
    )
    

admin.site.register(OrderPharm, OrderPharmAdmin)
admin.site.register(Pharmacy, PharmacyAdmin)