# Generated by Django 2.1.4 on 2018-12-15 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181106_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='car_color',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='car_comapany',
        ),
    ]
