# Generated by Django 2.1.2 on 2018-11-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carposition', '0002_auto_20181031_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positions',
            name='position_status',
            field=models.BooleanField(default=True, verbose_name='Parking status [default is unoccupied]'),
        ),
    ]
