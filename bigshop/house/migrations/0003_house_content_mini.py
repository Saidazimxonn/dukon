# Generated by Django 3.2 on 2021-09-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20210910_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='content_mini',
            field=models.TextField(default=1, verbose_name='Studio haqida malumot'),
            preserve_default=False,
        ),
    ]
