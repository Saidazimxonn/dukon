from django.contrib import admin
from .models import Bazar, Product, Market,Order
# Register your models here.
class BazarAdmin(admin.ModelAdmin):
    list_display = [
                'name'
    ]
class OrderAdmin(admin.ModelAdmin):
    list_display = [
                'name'
    ]
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id','name', 'market'
    ]
    list_filter = [
         'market'
    ]
class MarketAdmin(admin.ModelAdmin):
    list_display = [
        'id','name', 'bazar'
    ]
admin.site.register(Order, OrderAdmin)
admin.site.register(Bazar, BazarAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(Product, ProductAdmin)
