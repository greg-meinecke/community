# Generated by Django 5.1.1 on 2024-09-25 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Venue",
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
                ("address", models.CharField(max_length=256)),
                ("city", models.CharField(max_length=128)),
                ("state", models.CharField(max_length=32)),
                ("zip", models.CharField(max_length=16)),
                ("lat", models.FloatField(blank=True, null=True)),
                ("long", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=256)),
                ("url", models.URLField()),
                ("start_at", models.DateTimeField()),
                ("end_at", models.DateTimeField()),
                ("description", models.TextField()),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="groups.group"
                    ),
                ),
                (
                    "venue",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="events.venue",
                    ),
                ),
            ],
        ),
    ]