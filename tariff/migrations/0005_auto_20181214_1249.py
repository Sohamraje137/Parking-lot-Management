# Generated by Django 2.1.4 on 2018-12-14 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0004_auto_20181106_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='site_add',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carposition.Site'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='site_address',
            field=models.CharField(default='Not Parked', max_length=20, verbose_name=''),
        ),
    ]
