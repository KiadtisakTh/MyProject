# Generated by Django 4.2.7 on 2024-02-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_service', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelform',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
