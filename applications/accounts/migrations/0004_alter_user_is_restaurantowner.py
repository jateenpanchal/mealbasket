# Generated by Django 4.1.4 on 2023-02-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_user_is_active_user_is_staff_alter_user_is_superuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_restaurantowner",
            field=models.BooleanField(default=False, verbose_name="Is RestaurantOwner"),
        ),
    ]
