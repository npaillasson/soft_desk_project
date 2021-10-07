# Generated by Django 3.2.7 on 2021-10-07 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20211006_1648"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="assignee_user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assignee_user",
                to="api.contributor",
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="author_user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_user",
                to="api.contributor",
            ),
        ),
    ]
