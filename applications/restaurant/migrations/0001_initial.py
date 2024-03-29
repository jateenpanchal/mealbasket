# Generated by Django 4.1.4 on 2023-02-14 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mealbasketapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant_data",
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
                ("Restaurant_Name", models.CharField(max_length=100)),
                ("Restaurant_Email", models.EmailField(max_length=254)),
                (
                    "Restaurant_Type",
                    models.CharField(
                        choices=[
                            ("Veg", "Veg"),
                            ("Non-Veg", "Non-Veg"),
                            ("Both", "Both"),
                        ],
                        max_length=7,
                    ),
                ),
                ("Restaurant_Address", models.TextField()),
                ("Restaurant_GSTno", models.CharField(max_length=15)),
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
            name="fooditemdata",
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
                ("food_name", models.CharField(max_length=100)),
                ("food_price", models.CharField(max_length=5)),
                ("food_photo", models.ImageField(upload_to="img/food_picture/")),
                ("availability", models.BooleanField(default=False)),
                (
                    "category_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mealbasketapp.category",
                    ),
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
    ]
