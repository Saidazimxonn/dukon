from django.db import models

# Create your models here.
class Bazar(models.Model):
    name = models.CharField(verbose_name="Bazar name", max_length=200)

    def __str__(self):
        return self.name

class Market(models.Model):
    name = models.CharField(verbose_name="Name market", max_length=250)
    info_shop_product = models.CharField(verbose_name="Info and product", max_length=400)
    tg_link = models.CharField(verbose_name="Telegram link", max_length=200)
    locations = models.CharField(verbose_name="Market locations", max_length=200)
    info_long = models.TextField(verbose_name="Full info Market")
    phone = models.CharField(verbose_name="Telefon", max_length=50)
    phone2 = models.CharField(verbose_name="Telefon", max_length=50, null=True, blank=True)
    image = models.ImageField(verbose_name="Rasim")
    bazar = models.ForeignKey(Bazar, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="Mahsulot nomi", max_length=100)
    new_price = models.FloatField(verbose_name="Yangi narxi", default=0)
    old_price = models.FloatField(verbose_name="Oldingi narxi", default=0)
    new = models.BooleanField(verbose_name='Yangi mahsulot')
    sale = models.IntegerField(verbose_name="Chegirma", default=0)
    info_text = models.TextField(verbose_name="Mahsulot haqida To'liq")
    tg_link = models.CharField(verbose_name = "Telegram link", max_length=100)
    ins_link = models.CharField(verbose_name = "Instagram link", max_length=100, null=True, blank=True)
    phone = models.CharField(verbose_name="Telifon raqami", max_length=100)
    image = models.ImageField(verbose_name="Rasim")
    # bazar = models.ForeignKey(Bazar, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.SET_NULL, null=True, blank=True )
    
    def __str__(self):
        return self.name
