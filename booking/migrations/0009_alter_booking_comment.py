# Generated by Django 3.2.21 on 2023-10-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_booking_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='comment',
            field=models.TextField(blank=True, max_length=40),
        ),
    ]