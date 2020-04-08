from django.db import models
from django.contrib.auth.models import User
from course.models import Department, Course

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    entry_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.__str__()

class StudentTakesCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("student", "course"),)

    def __str__(self):
        return self.course.__str__() + ' '  + self.student.__str__()

