# Generated by Django 4.1 on 2022-08-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("page_title", models.TextField(verbose_name="текст записи")),
                ("pub_date", models.DateTimeField(verbose_name="дата записи")),
            ],
        ),
    ]
