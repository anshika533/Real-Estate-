# Generated by Django 5.2.4 on 2025-07-21 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_remove_lease_description_remove_lease_is_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lease',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
