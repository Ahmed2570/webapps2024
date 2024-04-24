# Generated by Django 4.2.11 on 2024-03-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("ACCEPTED", "Accepted"),
                    ("REJECTED", "Rejected"),
                    ("COMPLETED", "Completed"),
                ],
                default="PENDING",
                max_length=9,
            ),
        ),
    ]