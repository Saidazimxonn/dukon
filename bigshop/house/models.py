from django.db import models

# Create your models here.
class House(models.Model):
    name_company = models.CharField(verbose_name="Studia nomi",  max_length=255)
    name_product = models.CharField(verbose_name="Mahsulot nomi",  max_length=255)
    content = models.TextField(verbose_name="Studio haqida malumot va ximztlar")
    tg_link = models.CharField(verbose_name="Telegram link", max_length=255, null=True, blank=True)
    ins_link = models.CharField(verbose_name="Instagram link", max_length=255, null=True, blank=True)
    web_site = models.CharField(verbose_name="Web sayt", max_length=255, null=True, blank=True)
    phone = models.CharField(verbose_name='Telefon raqam', max_length=255)
    image = models.ImageField(verbose_name="Rasim", null=True, blank=True)
    image = models.ImageField(verbose_name="Rasim", null=True, blank=True)
    image2 = models.ImageField(verbose_name="Rasim2", null=True, blank=True)
    image3 = models.ImageField(verbose_name="Rasim3", null=True, blank=True)
    image4 = models.ImageField(verbose_name="Rasim4", null=True, blank=True)
    image5 = models.ImageField(verbose_name="Rasim5", null=True, blank=True)
    image6 = models.ImageField(verbose_name="Rasim6", null=True, blank=True)
    image7 = models.ImageField(verbose_name="Rasim7", null=True, blank=True)
    image8 = models.ImageField(verbose_name="Rasim8", null=True, blank=True)
    image9 = models.ImageField(verbose_name="Rasim9", null=True, blank=True)
    image10 = models.ImageField(verbose_name="Rasim10", null=True, blank=True)
    
    
    def __str__(self):
        return self.name_company
    class Meta:
      
        ordering = ['-id']
