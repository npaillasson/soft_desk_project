# Generated by Django 3.2.7 on 2021-10-13 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_alter_contributor_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="contributor",
            unique_together=set(),
        ),
    ]