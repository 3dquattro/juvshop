# Generated by Django 3.2.16 on 2023-01-26 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("my", "0009_auto_20230126_1351"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position",
            name="cart",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Корзина",
                to="my.cart",
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Заказ",
                to="my.order",
            ),
        ),
    ]