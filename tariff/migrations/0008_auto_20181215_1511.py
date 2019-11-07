# Generated by Django 2.1.4 on 2018-12-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0007_auto_20181215_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('Hour', 'Hour ticket')], max_length=20, verbose_name='Billing type')),
                ('per_hour_money', models.FloatField(default=10.0, verbose_name='Hourly parking fee')),
            ],
            options={
                'verbose_name': 'Tickets',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.AddField(
            model_name='tariffs',
            name='ticket_type',
            field=models.CharField(choices=[('Hour', 'Hour ticket')], default='hour', max_length=20, verbose_name='Billing type'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='site_address',
            field=models.CharField(default='Not Parked', max_length=20, verbose_name='Site Address'),
        ),
    ]
