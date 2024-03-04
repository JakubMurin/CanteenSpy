# Generated by Django 4.2.7 on 2023-11-26 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canteen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hours', models.TextField()),
                ('web', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(null=True)),
                ('day', models.DateField(null=True)),
                ('available', models.IntegerField(default=0)),
                ('unavailable', models.IntegerField(default=0)),
                ('meat', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
                ('canteen_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.canteen')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('menu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.menu')),
            ],
        ),
    ]