from django.db import models
from .choices import PROVINCES
# Create your models here.

class Pharmacy(models.Model):
    name = models.CharField(verbose_name="Dori nomi", max_length=100)
    pharmacy_info = models.CharField(verbose_name="Dori haqida qisqacha", max_length=400)
    tg_link = models.CharField(verbose_name="Telegram link", max_length=200)
    ins_link = models.CharField(verbose_name="Instagram link", max_length=200)
    new_price = models.FloatField(verbose_name="Yangi narxi", default=0)
    old_price = models.FloatField(verbose_name="Oldingi narxi", default=0)
    new = models.BooleanField(verbose_name='Yangi mahsulot')
    sale = models.IntegerField(verbose_name="Chegirma", default=0)
    content = models.TextField(verbose_name="To'lqi malumot")
    phone = models.CharField(verbose_name="Telefon", max_length=50)
    phone2 = models.CharField(verbose_name="Telefon", max_length=50, null=True, blank=True)
    image = models.ImageField(verbose_name="Rasim")
    locations = models.CharField(verbose_name="Dorixona  manzili", max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    
    name = models.CharField(verbose_name="Ism", max_length=255)
    phone = models.CharField(verbose_name="Telefon", max_length=255)
    province = models.CharField(verbose_name="Viloyat", max_length=50)
    count_product = models.IntegerField(verbose_name='Mahsulot soni', default=0)
    product_name = models.CharField(verbose_name="Mahsulot nomi", max_length=255, null=True, blank=True)
    price = models.CharField(verbose_name='Mahsulot narxi', max_length=255, null=True, blank=True)
    
    
    def __str__(self):
        return self.name

    