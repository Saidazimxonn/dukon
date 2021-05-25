from django.db import models

# Create your models here.
class Sections(models.Model):
    name = models.CharField(verbose_name="Bo'lim nomi", max_length=120)

    def __str__(self):
        return self.name



class Equipments(models.Model):
    name = models.CharField(verbose_name="Uskuna nomi", max_length=100)
    new_price = models.FloatField(verbose_name="Yangi narxi", default=0)
    old_price = models.FloatField(verbose_name="Oldingi narxi", default=0)
    new = models.BooleanField(verbose_name='Yangi mahsulot')
    sale = models.IntegerField(verbose_name="Chegirma", default=0)
    info_text = models.TextField(verbose_name="Mahsulot haqida To'liq")
    tg_link = models.CharField(verbose_name = "Telegram link", max_length=100)
    ins_link = models.CharField(verbose_name = "Instagram link", max_length=100, null=True, blank=True)
    phone = models.CharField(verbose_name="Telifon raqami", max_length=100)
    image = models.ImageField(verbose_name="Rasim")
    company = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name