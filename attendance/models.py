from django.db import models
import os

from student.models import Student
from faculty.models import Faculty
from course.models import Course, Timeslot

from datetime import datetime

# Returns the path of file
def get_file_path(instance, filename='img.jpg'):
	ext = filename.split('.')[-1]
	filename = "%s_%s.%s" % (str(instance.attendance.id), instance.attendance.date_time, ext)
	foldername = "%s" % ("Attendance_Image")
	return os.path.join(foldername, filename)

# Create your models here.
class Attendance(models.Model):
    date_time = models.DateTimeField(default= datetime.now())

    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(Timeslot, null=True, on_delete=models.SET_NULL) 

    class Meta:
        unique_together = (("date_time", "faculty", "course"),)

    def __str__(self):
        return self.course.__str__() + ' ' + str(self.date_time) + ' '  + self.faculty.__str__()

class AttendanceImage(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)

class AttendanceStudents(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
 
