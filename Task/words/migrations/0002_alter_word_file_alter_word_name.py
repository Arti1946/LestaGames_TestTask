# Generated by Django 5.0.3 on 2024-04-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("words", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="word",
            name="file",
            field=models.FileField(unique=True, upload_to="media/files/"),
        ),
        migrations.AlterField(
            model_name="word",
            name="name",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]