# Generated by Django 4.1.7 on 2023-03-29 12:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen_service", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cook",
            name="years_of_experience",
        ),
    ]
