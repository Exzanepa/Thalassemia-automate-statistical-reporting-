# Generated by Django 4.1.3 on 2023-02-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_general", "0006_alter_noisemap_data_x_alter_noisemap_data_y_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="noisemap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("x", models.PositiveIntegerField(default=0)),
                ("y", models.PositiveIntegerField(default=0)),
                ("z", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name="noisemap_data",
        ),
    ]
