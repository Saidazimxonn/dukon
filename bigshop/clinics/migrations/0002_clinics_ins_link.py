# Generated by Django 3.2 on 2021-05-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinics',
            name='ins_link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram link'),
        ),
    ]
