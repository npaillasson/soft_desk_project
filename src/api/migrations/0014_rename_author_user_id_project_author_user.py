# Generated by Django 3.2.7 on 2021-10-13 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_alter_project_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="author_user_id",
            new_name="author_user",
        ),
    ]