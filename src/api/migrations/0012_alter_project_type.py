# Generated by Django 3.2.7 on 2021-10-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_alter_project_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="type",
            field=models.CharField(max_length=30),
        ),
    ]
