from django.contrib import admin

# Register your models here.
from .models import Company, Product

class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'image_tag'
    ]



admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)