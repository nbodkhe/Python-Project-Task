# Generated by Django 5.0.1 on 2024-02-01 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food_orders", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("f_name", models.CharField(max_length=255)),
                ("l_name", models.CharField(blank=True, max_length=255)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("image", models.URLField(blank=True, null=True)),
                ("is_phone_verified", models.BooleanField(default=False)),
                ("email_verified_at", models.DateTimeField(blank=True, null=True)),
                (
                    "email_verification_token",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("cm_firebase_token", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("status", models.IntegerField()),
                ("order_count", models.IntegerField()),
                ("emp_id", models.CharField(max_length=20)),
                ("department_id", models.IntegerField()),
                ("is_veg", models.BooleanField(default=False)),
                ("is_sat_opted", models.BooleanField(default=False)),
                ("device_id", models.CharField(max_length=255)),
                ("is_invalid_device", models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name="foodorder",
            name="employee",
        ),
        migrations.CreateModel(
            name="Report",
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
                ("date", models.DateField()),
                ("breakfast", models.CharField(blank=True, max_length=20, null=True)),
                ("lunch", models.CharField(blank=True, max_length=20, null=True)),
                ("dinner", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_orders.user",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.DeleteModel(
            name="FoodOrder",
        ),
    ]
