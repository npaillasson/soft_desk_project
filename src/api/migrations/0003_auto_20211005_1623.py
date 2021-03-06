# Generated by Django 3.2.7 on 2021-10-05 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_auto_20211004_1721"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contributor",
            name="body",
        ),
        migrations.AlterField(
            model_name="contributor",
            name="project_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contributors",
                to="api.project",
            ),
        ),
    ]
