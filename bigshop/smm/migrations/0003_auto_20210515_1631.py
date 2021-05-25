# Generated by Django 3.2 on 2021-05-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smm', '0002_smm_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='smm',
            name='ins_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Instagram link'),
        ),
        migrations.AddField(
            model_name='smm',
            name='web_site',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Web sayt'),
        ),
        migrations.AlterField(
            model_name='smm',
            name='tg_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegram link'),
        ),
    ]