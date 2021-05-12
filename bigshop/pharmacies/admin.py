from django.contrib import admin
from .models import Pharmacy, Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display=(
        'product_name', 'name', 'phone' , 'count_product', 'province'
    )
   
    list_display_links=(
        'product_name', 'name', 'phone' , 'count_product', 'province'
    )
 
   

class PharmacyAdmin(admin.ModelAdmin):
    list_display=(
        'name', 'pharmacy_info'
    )
    

admin.site.register(Order, OrderAdmin)
admin.site.register(Pharmacy, PharmacyAdmin)