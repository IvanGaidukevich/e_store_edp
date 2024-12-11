# Generated by Django 5.0.6 on 2024-12-11 16:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coupon",
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
                (
                    "code",
                    models.CharField(
                        max_length=16, unique=True, verbose_name="Промокод"
                    ),
                ),
                ("valid_from", models.DateTimeField(verbose_name="Начало действия")),
                ("valid_to", models.DateTimeField(verbose_name="Конец действия")),
                (
                    "discount",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]