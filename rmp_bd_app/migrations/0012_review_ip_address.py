# Generated by Django 3.2.7 on 2021-11-19 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmp_bd_app', '0011_auto_20211118_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ip_address',
            field=models.CharField(default='0.0.0.0', max_length=15),
            preserve_default=False,
        ),
    ]
