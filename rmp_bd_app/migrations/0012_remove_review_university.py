# Generated by Django 3.2.8 on 2021-10-28 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmp_bd_app', '0011_auto_20211027_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='university',
        ),
    ]
