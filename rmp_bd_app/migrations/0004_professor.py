# Generated by Django 3.2.7 on 2021-11-14 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmp_bd_app', '0003_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('honorific', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.campus')),
            ],
            options={
                'verbose_name_plural': 'professors',
            },
        ),
        migrations.AddField(
            model_name='professor',
            name='current_university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.university'),
        ),
        migrations.AddField(
            model_name='professor',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.department'),
        ),
    ]
