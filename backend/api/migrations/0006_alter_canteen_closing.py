# Generated by Django 4.2.7 on 2023-12-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_canteen_closing_canteen_low_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canteen',
            name='closing',
            field=models.CharField(default='16:00', max_length=10),
        ),
    ]
