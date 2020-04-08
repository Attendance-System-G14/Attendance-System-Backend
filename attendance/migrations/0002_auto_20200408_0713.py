# Generated by Django 3.0.4 on 2020-04-08 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0001_initial'),
        ('faculty', '0001_initial'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='faculty.Faculty'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='timeslot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Timeslot'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('date', 'time', 'student', 'course')},
        ),
    ]