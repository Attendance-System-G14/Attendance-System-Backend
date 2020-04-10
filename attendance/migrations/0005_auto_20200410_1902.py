# Generated by Django 3.0.4 on 2020-04-10 19:02

import attendance.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200408_0713'),
        ('student', '0001_initial'),
        ('faculty', '0001_initial'),
        ('attendance', '0004_auto_20200410_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 19, 2, 58, 948103)),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('date_time', 'faculty', 'course')},
        ),
        migrations.CreateModel(
            name='AttendanceStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Attendance')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=attendance.models.get_file_path)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Attendance')),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
    ]
