# Generated by Django 3.2.5 on 2021-07-16 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0002_driver_ride'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
