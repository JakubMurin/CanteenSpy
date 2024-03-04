# Generated by Django 4.2.7 on 2023-12-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_menu_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='canteen',
            old_name='location',
            new_name='address',
        ),
        migrations.AddField(
            model_name='canteen',
            name='avg_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='canteen',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='avg_rating',
            field=models.IntegerField(default=0),
        ),
    ]