from django.contrib import admin

# Register your models here.
from .models import LiveMessage, Reklama

class LiveMessageAdmin(admin.ModelAdmin):
    list_display =(
        'name', 'full_name', 'phone', 'message'
    )
    list_display_links = (
                'name', 'full_name', 'phone', 'message'
    )

admin.site.register(LiveMessage, LiveMessageAdmin)
class ReklamaAdmin(admin.ModelAdmin):
    list_display =(
       'title',
    )
    list_display_links = (
                   'title',
    )

admin.site.register(Reklama, ReklamaAdmin)