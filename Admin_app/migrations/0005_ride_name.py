# Generated by Django 3.2.5 on 2021-07-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0004_auto_20210716_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='Name',
            field=models.CharField(default=1, max_length=128),
        ),
    ]