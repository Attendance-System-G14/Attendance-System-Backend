from django.db import models

from student.models import Student
from faculty.models import Faculty
from course.models import Course, Timeslot

# Create your models here.
class Attendance(models.Model):
    date = models.DateField()
    time = models.TimeField(auto_now=True)

    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL) 

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(Timeslot, null=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return self.course.__str__() + ' ' + str(self.date) + ' '  + self.student.__str__()
