# Generated by Django 3.2 on 2021-04-29 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_auto_20210429_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='bazar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sellers.bazar'),
            preserve_default=False,
        ),
    ]
