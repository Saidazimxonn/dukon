from django.contrib import admin
from django.db.models import fields
from .models import SMM
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
# Register your models here.

class FormAdminSmm(forms.ModelForm):
    content = forms.CharField(label="Ma'lumot", widget=CKEditorUploadingWidget())


    class Meta():
        fields = '__all__'


@admin.register(SMM)
class HouseAmin(admin.ModelAdmin):
    form = FormAdminSmm
