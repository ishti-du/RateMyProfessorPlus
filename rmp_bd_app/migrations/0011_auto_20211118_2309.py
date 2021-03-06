# Generated by Django 3.2.7 on 2021-11-19 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rmp_bd_app', '0010_auto_20211118_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thumbdown',
            options={},
        ),
        migrations.CreateModel(
            name='ReportFlag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='report_flags', to='rmp_bd_app.review')),
                ('users', models.ManyToManyField(related_name='report_flags', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'reviews',
            },
        ),
    ]
