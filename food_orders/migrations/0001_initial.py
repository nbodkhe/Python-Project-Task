# Generated by Django 5.0.1 on 2024-01-31 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("f_name", models.CharField(max_length=100)),
                ("l_name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("status", models.IntegerField()),
                ("order_count", models.IntegerField()),
                ("emp_id", models.CharField(max_length=20)),
                ("department_id", models.IntegerField()),
                ("is_veg", models.BooleanField()),
                ("is_sat_opted", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="FoodOrder",
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
                ("breakfast", models.CharField(max_length=20)),
                ("lunch", models.CharField(max_length=20)),
                ("dinner", models.CharField(max_length=20)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="food_orders.employee",
                    ),
                ),
            ],
        ),
    ]