# Generated by Django 3.2.7 on 2021-10-04 15:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Contributors',
            new_name='Contributor',
        ),
        migrations.RenameModel(
            old_name='Issues',
            new_name='Issue',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]