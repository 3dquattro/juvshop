# Generated by Django 3.2.16 on 2022-12-20 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_alter_jewelry_id"),
        ("my", "0002_message_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="jewelry",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.jewelry",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="jewelry",
            field=models.ManyToManyField(blank=True, to="core.Jewelry"),
        ),
    ]
