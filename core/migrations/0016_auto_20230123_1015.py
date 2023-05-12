# Generated by Django 3.2.16 on 2023-01-23 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0015_alter_material_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="jewelry",
            name="status",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="jewelry",
            name="update_time",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="material",
            name="status",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="material",
            name="update_time",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="part",
            name="status",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="part",
            name="update_time",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="parttype",
            name="status",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="parttype",
            name="update_time",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="producttype",
            name="status",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="producttype",
            name="update_time",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="user",
            name="status",
            field=models.IntegerField(default=0),
        ),
    ]
