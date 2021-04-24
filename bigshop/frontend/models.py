from django.db import models

# Create your models here.
class LiveMessage(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    full_name = models.CharField(verbose_name="Full name", max_length=100)
    phone = models.CharField(verbose_name="Phone", max_length=100)
    message = models.CharField(verbose_name="Message", max_length=100)
    message_long = models.TextField(verbose_name="Message long")

    def __str__(self):
        return self.name