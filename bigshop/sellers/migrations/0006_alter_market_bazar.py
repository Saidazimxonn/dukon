# Generated by Django 3.2 on 2021-05-03 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0005_market_phone2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='bazar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sellers.bazar'),
        ),
    ]
