# Generated by Django 3.2 on 2021-05-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacies', '0003_auto_20210509_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='province',
            field=models.CharField(max_length=50, verbose_name='Viloyat'),
        ),
    ]
