from django.db import models

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

LECTURE_TYPES = (
    (0, 'Lecture'),
    (1, 'Tutorial')
)

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Timeslot(models.Model):
    name = models.CharField(max_length=1, primary_key=True)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Timeslot, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class TimeSlotDetails(models.Model):
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)

    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    lecture_type = models.CharField(max_length=1, choices=LECTURE_TYPES)

    def __str__(self):
        return self.timeslot.__str__() + ' '  + self.day + ' '  + str(self.start_time)

class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
   
    course_coordinator = models.ForeignKey('faculty.Faculty', null=True, on_delete=models.CASCADE)  #To avoid circular imports
    timeslot = models.ForeignKey(Timeslot, null=True, on_delete=models.SET_NULL)


    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.code + ' ' + self.name
