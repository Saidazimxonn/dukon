# Generated by Django 3.2 on 2021-04-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_company_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ins_link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram link'),
        ),
    ]