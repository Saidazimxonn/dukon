# Generated by Django 3.2 on 2021-04-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ins_link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram link'),
        ),
    ]
