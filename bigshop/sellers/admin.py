from django.contrib import admin
from .models import Bazar, Product, Market,Order, Ad_product
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
class Ad_productAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)
admin.site.register(Bazar, BazarAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Ad_product, Ad_productAdmin)