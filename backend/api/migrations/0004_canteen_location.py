# Generated by Django 4.2.7 on 2023-12-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_location_canteen_address_canteen_avg_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='canteen',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
