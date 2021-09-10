from django.contrib import admin
from django.forms import forms
from .models import House
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from django import forms
# Register your models here.
class HouseAdminForm(forms.ModelForm):
    content = forms.CharField(label="Ma'lumot" ,widget=CKEditorUploadingWidget())
    
    class Meta:
        model = House
        fields = '__all__'




@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    form = HouseAdminForm


