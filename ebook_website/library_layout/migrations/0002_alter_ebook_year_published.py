# Generated by Django 4.1.3 on 2022-12-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library_layout", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ebook",
            name="year_published",
            field=models.IntegerField(max_length=64),
        ),
    ]