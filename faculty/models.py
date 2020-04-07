from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faculty(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('course.Department', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.__str__()

class FacultyTakesCourse(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Course = models.ForeignKey('course.Course', on_delete=models.CASCADE)