# Generated by Django 3.2 on 2021-09-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0009_auto_20210903_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad_product',
            options={'verbose_name': 'Yangi tovar ', 'verbose_name_plural': 'Yangi tovarlar '},
        ),
        migrations.AddField(
            model_name='order',
            name='new_p',
            field=models.BooleanField(blank=True, null=True, verbose_name='Yangi'),
        ),
    ]