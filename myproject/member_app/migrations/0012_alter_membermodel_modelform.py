# Generated by Django 4.2.7 on 2024-03-29 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("form_service", "0013_alter_modelform_status"),
        ("member_app", "0011_membermodel_modelform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membermodel",
            name="modelform",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="form_service.modelform",
            ),
        ),
    ]
