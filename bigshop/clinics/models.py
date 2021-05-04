from django.db import models

# Create your models here.
class Categorys(models.Model):
    name = models.CharField(verbose_name="Toifa nomi", max_length=250)

    def __str__(self):
        return self.name

class Clinics(models.Model):
    name = models.CharField(verbose_name="Klinika nomi", max_length=250)
    info_service = models.CharField(verbose_name="Xizmatlar", max_length=500)
    tg_link = models.CharField(verbose_name="Telegram link", max_length=200)
    ins_link = models.CharField(verbose_name = "Instagram link", max_length=100, null=True, blank=True)
    locations = models.CharField(verbose_name="Klinika manzili", max_length=200)
    info_long = models.TextField(verbose_name="Klinika haqida to‘liq maʼlumot")
    phone = models.CharField(verbose_name="Telefon", max_length=50)
    phone2 = models.CharField(verbose_name="Ikkinchi telefon raqam ", max_length=50, null=True, blank=True)
    image = models.ImageField(verbose_name="Rasim")
    category = models.ForeignKey(Categorys, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')

    def __str__(self):
        return self.name


    