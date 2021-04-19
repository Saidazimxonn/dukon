from os import name
from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.html import mark_safe
# Create your models here.
class Company(models.Model):
    
    name = models.CharField(verbose_name="Korxona nomi", max_length=100)
    name_long = models.CharField(verbose_name="Korxona To'liq nomi", max_length=500)
    tg_link = models.CharField(verbose_name = "Telegram link", max_length=100)
    ins_link = models.CharField(verbose_name = "Instagram link", max_length=100, null=True, blank=True)
    phone = models.CharField(verbose_name="Telifon raqami", max_length=100)
    image = models.ImageField(verbose_name="Rasim")
    info = models.TextField(verbose_name="Korxona haqida", )





    def __str__(self):
        return self.name





class Product(models.Model):

    name = models.CharField(verbose_name = "Mahsulot nomi", max_length=100)
    new_price = models.FloatField(verbose_name="Yangi narxi", default=0)
    old_price = models.FloatField(verbose_name="Eski narxi", default=0)
    new = models.BooleanField(verbose_name='Yangi mahsulot')
    sale = models.IntegerField(verbose_name="Chegirma", default=0)
    info = models.CharField(verbose_name = "Mahsulot haqida qisqa", max_length=500)
    info_text = models.TextField(verbose_name="Mahsulot haqida To'liq")
    tg_link = models.CharField(verbose_name = "Telegram link", max_length=100)
    ins_link = models.CharField(verbose_name = "Instagram link", max_length=100, null=True, blank=True)
    phone = models.CharField(verbose_name="Telifon raqami", max_length=100)
    image = models.ImageField(verbose_name="Rasim")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def image_tag(self):
            return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'
    def __str__(self):
        return self.name
    

