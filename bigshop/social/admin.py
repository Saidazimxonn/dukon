from django.contrib import admin
from .models import Categorya_M, Messanger
# Register your models here.
class CategoryaMAdmin(admin.ModelAdmin):
    list_display=[
        'name'
    ]
class MessangerAdmin(admin.ModelAdmin):
    list_display=[
        'name'
    ]
admin.site.register(Categorya_M, CategoryaMAdmin)
admin.site.register(Messanger, MessangerAdmin)