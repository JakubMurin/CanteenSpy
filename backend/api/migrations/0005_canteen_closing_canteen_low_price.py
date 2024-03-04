# Generated by Django 4.2.7 on 2023-12-10 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_canteen_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='canteen',
            name='closing',
            field=models.TimeField(default=datetime.time(16, 0)),
        ),
        migrations.AddField(
            model_name='canteen',
            name='low_price',
            field=models.DecimalField(decimal_places=2, default=4.2, max_digits=10),
        ),
    ]
