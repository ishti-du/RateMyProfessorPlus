# Generated by Django 3.2.8 on 2021-10-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmp_bd_app', '0015_alter_review_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='tags',
            field=models.CharField(choices=[(1, 'Yay'), (2, 'Oh')], max_length=15),
        ),
    ]