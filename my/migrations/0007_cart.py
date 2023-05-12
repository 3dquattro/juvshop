# Generated by Django 3.2.16 on 2023-01-25 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_auto_20230123_1015"),
        ("my", "0006_auto_20230123_1015"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="core.user",
                    ),
                ),
                ("order_date", models.DateTimeField()),
                ("update_time", models.DateTimeField()),
                ("status", models.IntegerField(default=0)),
            ],
        ),
    ]