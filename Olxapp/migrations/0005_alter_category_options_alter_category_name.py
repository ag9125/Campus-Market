# Generated by Django 5.0.3 on 2024-03-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Olxapp', '0004_recipe_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
