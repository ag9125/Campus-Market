# Generated by Django 5.0.3 on 2024-04-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Olxapp', '0009_rename_recipe_olx'),
    ]

    operations = [
        migrations.AddField(
            model_name='olx',
            name='Approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]
