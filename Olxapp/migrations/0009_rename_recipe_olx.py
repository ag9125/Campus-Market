# Generated by Django 5.0.3 on 2024-04-13 18:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Olxapp', '0008_rename_image_image_upload_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='recipe',
            new_name='Olx',
        ),
    ]
