from django.contrib import admin

# Register your models here.
from .models import Categorya, Chanel_Group

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
class ChanelAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

admin.site.register(Categorya, CategoryAdmin)
admin.site.register(Chanel_Group, ChanelAdmin)