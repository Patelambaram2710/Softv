# Generated by Django 5.1 on 2024-08-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("category", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=100)),
                ("quantity", models.IntegerField()),
                ("image", models.ImageField(upload_to="products/")),
                ("desc", models.CharField(max_length=300)),
                ("price", models.IntegerField()),
            ],
        ),
    ]
