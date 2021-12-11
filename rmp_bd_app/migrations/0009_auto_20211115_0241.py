# Generated by Django 3.2.7 on 2021-11-15 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rmp_bd_app', '0008_auto_20211027_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='is_attendance',
        ),
        migrations.AddField(
            model_name='review',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Gives Good Feedback', 'Gives Good Feedback'), ('Lots of Homework', 'Lots of Homework'), ('Accessible Outside of Class', 'Accessible Outside of Class'), ('Attendance Mandatory', 'Attendance Mandatory'), ('Inspirational', 'Inspirational'), ('Test Heavy', 'Test Heavy'), ('Lecture Heavy', 'Lecture Heavy'), ('Extra Credit', 'Extra Credit'), ('Clear Grading Criteria', 'Clear Grading Criteria'), ('Pop Quizzes', 'Pop Quizzes'), ('Caring', 'Caring')], max_length=179, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='campus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.campus'),
        ),
        migrations.AlterField(
            model_name='review',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rmp_bd_app.course'),
        ),
        migrations.AlterField(
            model_name='review',
            name='glad_text',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='review',
            name='mad_text',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='review',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.professor'),
        ),
        migrations.AlterField(
            model_name='review',
            name='sad_text',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='review',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.university'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
