# Generated by Django 4.2.2 on 2023-06-10 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="myModel",
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
                ("field1", models.CharField(max_length=100)),
                ("field2", models.CharField(max_length=100)),
                ("field3", models.CharField(max_length=100)),
                ("field4", models.CharField(max_length=100)),
            ],
        ),
    ]