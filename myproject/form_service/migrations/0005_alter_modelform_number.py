# Generated by Django 4.2.7 on 2024-02-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_service', '0004_modelform_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelform',
            name='number',
            field=models.IntegerField(max_length=10),
        ),
    ]
