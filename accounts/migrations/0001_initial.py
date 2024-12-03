# Generated by Django 5.0.6 on 2024-11-26 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                (
                    "address",
                    models.CharField(max_length=255, verbose_name="Улица, дом"),
                ),
                (
                    "postal_code",
                    models.CharField(max_length=12, verbose_name="Почтовый индекс"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "tel",
                    models.CharField(blank=True, max_length=11, verbose_name="Телефон"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Профайл",
                "verbose_name_plural": "Профайлы",
            },
        ),
    ]