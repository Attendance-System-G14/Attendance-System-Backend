from django.db import models

from student.models import Student
from faculty.models import Faculty
from course.models import Course, Timeslot

from datetime import datetime

# Create your models here.
class Attendance(models.Model):
    date_time = models.DateTimeField(default= datetime.now())

    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(Timeslot, null=True, on_delete=models.SET_NULL) 

    class Meta:
        unique_together = (("date_time", "student", "course"),)

    def __str__(self):
        return self.course.__str__() + ' ' + str(self.date_time) + ' '  + self.student.__str__()
