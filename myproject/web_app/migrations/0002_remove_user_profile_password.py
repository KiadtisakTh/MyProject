# Generated by Django 4.2.7 on 2024-03-25 03:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user_profile",
            name="password",
        ),
    ]