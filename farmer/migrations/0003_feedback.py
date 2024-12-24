# Generated by Django 5.1.2 on 2024-10-19 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmer", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("feedback_name", models.CharField(max_length=40)),
                ("feedback", models.CharField(max_length=40)),
                ("date", models.DateField()),
            ],
        ),
    ]