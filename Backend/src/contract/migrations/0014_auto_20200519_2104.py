# Generated by Django 3.0.3 on 2020-05-19 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0013_auto_20200519_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='overdue',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='deadDatePay',
            field=models.DateField(default=datetime.datetime(2020, 5, 29, 21, 4, 12, 39949)),
        ),
    ]