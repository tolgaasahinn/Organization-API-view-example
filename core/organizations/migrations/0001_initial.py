# Generated by Django 4.1.1 on 2022-09-08 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("organisation_name", models.CharField(max_length=150)),
                (
                    "organization_logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="organization_logos/%Y/%m/"
                    ),
                ),
                (
                    "organization_type",
                    models.CharField(
                        choices=[
                            ("Person", "Person"),
                            ("Conglomerate", "Conglomerate"),
                            ("KOBİ", "KOBİ"),
                            ("STK", "STK"),
                        ],
                        max_length=15,
                    ),
                ),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("organization_url", models.URLField()),
                ("number_of_employees", models.IntegerField(default=1)),
                (
                    "organisations_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organisations_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]