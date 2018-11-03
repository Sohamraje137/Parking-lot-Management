# Generated by Django 2.1.2 on 2018-10-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_per_time', models.FloatField(default='40.00', verbose_name='Pay charges')),
            ],
            options={
                'verbose_name_plural': 'Rates',
                'verbose_name': 'Rates',
            },
        ),
    ]
