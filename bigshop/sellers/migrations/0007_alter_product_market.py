# Generated by Django 3.2 on 2021-06-03 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0006_alter_market_bazar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sellers.market'),
        ),
    ]
