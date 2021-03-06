# Generated by Django 3.2.7 on 2021-10-06 00:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmp_bd_app', '0003_auto_20200404_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'campuses',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=10)),
                ('course_title', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('honorific', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.campus')),
            ],
            options={
                'verbose_name_plural': 'professors',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('F', 'F'), ('Drop/Withdrawal', 'Drop/Withdrawal'), ('Incomplete', 'Incomplete'), ('Not sure yet', 'Not sure yet'), ('Rather not say', 'Rather not say'), ('Audit/No Grade', 'Audit/No Grade')], max_length=15)),
                ('thumbs_up', models.IntegerField(default=0)),
                ('thumbs_down', models.IntegerField(default=0)),
                ('report_flags', models.IntegerField(default=0)),
                ('mad_text', models.CharField(max_length=350)),
                ('sad_text', models.CharField(max_length=350)),
                ('glad_text', models.CharField(max_length=350)),
                ('difficulty_level', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('professor_score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('semester', models.CharField(choices=[('WNTR', 'Winter'), ('SPR', 'Spring'), ('SMR', 'Summer'), ('FALL', 'Fall')], max_length=4)),
                ('year', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021)),
                ('is_textbook', models.BooleanField()),
                ('is_attendance', models.BooleanField()),
                ('is_credit', models.BooleanField()),
                ('is_online', models.BooleanField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.campus')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rmp_bd_app.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.professor')),
            ],
            options={
                'verbose_name_plural': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=320)),
                ('password', models.CharField(max_length=128)),
                ('role', models.IntegerField(choices=[(0, 'student'), (1, 'professor'), (2, 'admin')], default=0)),
                ('ip_address', models.CharField(max_length=15)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='department_name',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='university',
            new_name='university_name',
        ),
        migrations.CreateModel(
            name='Review_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.review')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.tag')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.user'),
        ),
        migrations.CreateModel(
            name='Professor_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.professor')),
            ],
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
        migrations.CreateModel(
            name='Prereq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_id', to='rmp_bd_app.course')),
                ('prereq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prereq_id', to='rmp_bd_app.course')),
            ],
            options={
                'verbose_name_plural': 'prerequisites',
            },
        ),
        migrations.CreateModel(
            name='Campus_Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.campus')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.professor')),
            ],
        ),
        migrations.AddField(
            model_name='campus',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp_bd_app.university'),
        ),
    ]
