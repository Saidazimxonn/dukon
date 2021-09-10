from django.db import models

# Create your models here.
class House(models.Model):
    name_company = models.CharField(verbose_name="Studia nomi",  max_length=255)
    name_product = models.CharField(verbose_name="Mahsulot nomi",  max_length=255)
    content = models.TextField(verbose_name="Studio haqida malumot va ximztlar")
    content_mini = models.TextField(verbose_name='Studio haqida malumot')
    tg_link = models.CharField(verbose_name="Telegram link", max_length=255, null=True, blank=True)
    ins_link = models.CharField(verbose_name="Instagram link", max_length=255, null=True, blank=True)
    web_site = models.CharField(verbose_name="Web sayt", max_length=255, null=True, blank=True)
    phone = models.CharField(verbose_name='Telefon raqam', max_length=255)
    image = models.ImageField(verbose_name="Rasim", null=True, blank=True)
   
    
    
    def __str__(self):
        return self.name_company
    class Meta:
        verbose_name = 'Uy'
        verbose_name_plural = 'Uylar'
        
        
        ordering = ['-id']
