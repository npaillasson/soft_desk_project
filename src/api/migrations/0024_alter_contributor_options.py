# Generated by Django 3.2.7 on 2021-10-13 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0023_auto_20211013_1611"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contributor",
            options={"ordering": ["permission"]},
        ),
    ]
