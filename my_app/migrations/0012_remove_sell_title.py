# Generated by Django 5.2.4 on 2025-07-23 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_sell_area_sell_email_sell_mobile_sell_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='title',
        ),
    ]
