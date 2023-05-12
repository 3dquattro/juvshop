# Generated by Django 3.2.16 on 2022-11-03 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_auto_20221102_2124"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="part",
            name="productType",
        ),
        migrations.AlterField(
            model_name="part",
            name="ModelFile",
            field=models.FileField(upload_to="parts/"),
        ),
        migrations.CreateModel(
            name="PartType",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=60)),
                (
                    "productType",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.producttype",
                    ),
                ),
            ],
        ),
        # migrations.AddField(
        #    model_name='part',
        #    name='partType',
        #    field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.parttype'),
        #    preserve_default=False,
        # ),
    ]
