# Generated by Django 5.0.3 on 2024-03-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Olxapp', '0007_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='Upload_image',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='Upload_image',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='image/'),
        ),
    ]
