# Generated by Django 3.2.21 on 2023-09-28 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20230925_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='guest',
            new_name='guests',
        ),
    ]
