# Generated by Django 3.2 on 2021-04-29 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bazar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Bazar name')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name market')),
                ('info_shop_product', models.CharField(max_length=400, verbose_name='Info and product')),
                ('tg_link', models.CharField(max_length=200, verbose_name='Telegram link')),
                ('locations', models.CharField(max_length=200, verbose_name='Market locations')),
                ('info_long', models.TextField(verbose_name='Full info Market')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon')),
                ('image', models.ImageField(upload_to='', verbose_name='Rasim')),
                ('bazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.bazar')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mahsulot nomi')),
                ('new_price', models.FloatField(default=0, verbose_name='Yangi narxi')),
                ('old_price', models.FloatField(default=0, verbose_name='Oldingi narxi')),
                ('new', models.BooleanField(verbose_name='Yangi mahsulot')),
                ('sale', models.IntegerField(default=0, verbose_name='Chegirma')),
                ('info_text', models.TextField(verbose_name="Mahsulot haqida To'liq")),
                ('tg_link', models.CharField(max_length=100, verbose_name='Telegram link')),
                ('ins_link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram link')),
                ('phone', models.CharField(max_length=100, verbose_name='Telifon raqami')),
                ('image', models.ImageField(upload_to='', verbose_name='Rasim')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.market')),
            ],
        ),
    ]
