# Generated by Django 3.2 on 2021-04-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0003_market_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='phone',
            field=models.CharField(default=1, max_length=50, verbose_name='Telefon'),
            preserve_default=False,
        ),
    ]