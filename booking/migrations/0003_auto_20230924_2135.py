# Generated by Django 3.2.21 on 2023-09-24 21:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='table',
        ),
        migrations.AddField(
            model_name='booking',
            name='day',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='guest', max_length=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00')], default='time', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='comment',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
