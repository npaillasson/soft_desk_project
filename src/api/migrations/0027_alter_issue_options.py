# Generated by Django 3.2.7 on 2021-10-13 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0026_alter_issue_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="issue",
            options={"ordering": ["status", "priority", "created_time"]},
        ),
    ]
