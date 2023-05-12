# Generated by Django 3.2.16 on 2022-11-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="login",
            new_name="email",
        ),
        migrations.AddField(
            model_name="user",
            name="create_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="update_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]