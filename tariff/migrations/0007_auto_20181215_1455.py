# Generated by Django 2.1.4 on 2018-12-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0006_auto_20181215_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffs',
            name='site_address',
            field=models.CharField(default='Not Parked', max_length=20, verbose_name='Site address'),
        ),
    ]
