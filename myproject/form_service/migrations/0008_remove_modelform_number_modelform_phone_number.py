# Generated by Django 4.2.7 on 2024-02-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("form_service", "0007_alter_modelform_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modelform",
            name="number",
        ),
        migrations.AddField(
            model_name="modelform",
            name="phone_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
