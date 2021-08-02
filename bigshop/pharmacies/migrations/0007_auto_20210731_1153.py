# Generated by Django 3.2 on 2021-07-31 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacies', '0006_alter_order_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPharm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ism')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefon')),
                ('province', models.CharField(max_length=50, verbose_name='Viloyat')),
                ('count_product', models.IntegerField(default=0, verbose_name='Mahsulot soni')),
                ('product_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mahsulot nomi')),
                ('price', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mahsulot narxi')),
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
            },
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AlterModelOptions(
            name='pharmacy',
            options={'verbose_name': 'Dori', 'verbose_name_plural': 'Dorilar'},
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
