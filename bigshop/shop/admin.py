from django.contrib import admin

# Register your models here.
from .models import Company, Product

class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'name','id'
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'image_tag'
    ]
    list_filter = [
        'company'
    ]



admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)