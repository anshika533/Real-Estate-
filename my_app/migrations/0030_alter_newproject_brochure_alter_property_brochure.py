# Generated by Django 5.2.4 on 2025-07-25 10:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0029_alter_newproject_brochure_alter_newproject_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newproject',
            name='brochure',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='brochure',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
