# Generated by Django 3.2 on 2021-09-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['-id'], 'verbose_name': 'Uy', 'verbose_name_plural': 'Uylar'},
        ),
        migrations.RemoveField(
            model_name='house',
            name='image10',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image7',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image8',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image9',
        ),
        migrations.AlterField(
            model_name='house',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]