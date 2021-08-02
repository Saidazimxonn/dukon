from django.db import models

# Create your models here.
class Sections(models.Model):
    name = models.CharField(verbose_name="Bo'lim nomi", max_length=120)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Bo\'lim'
        verbose_name_plural = 'Bo\'limlar'


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
    class Meta:
        verbose_name = 'Uskuna'
        verbose_name_plural = 'Uskunalar'
    
class Order(models.Model):
    
    name = models.CharField(verbose_name="Ism", max_length=255)
    phone = models.CharField(verbose_name="Telefon", max_length=255)
    province = models.CharField(verbose_name="Viloyat", max_length=50)
    count_product = models.IntegerField(verbose_name='Mahsulot soni', default=0)
    product_name = models.CharField(verbose_name="Mahsulot nomi", max_length=255, null=True, blank=True)
    price = models.CharField(verbose_name='Mahsulot narxi', max_length=255, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'