# Generated by Django 2.1.4 on 2018-12-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181215_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='car_color',
            field=models.CharField(default='', max_length=8, verbose_name='Car color'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='car_comapany',
            field=models.CharField(default='', max_length=8, verbose_name='Car company'),
        ),
    ]
