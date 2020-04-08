from django.test import TestCase
from django.contrib.auth.models import User
from course.models import Department, Timeslot, TimeSlotDetails, Course
from faculty.models import Faculty
import datetime

class TestModels(TestCase):

    def setUp(self):
        self.department_name1= 'Computer Science and Engineering'
        self.timeslot1_name= 'a'
        self.timeslot1_day= 1
        self.timeslot1_start_time= datetime.time(hour=8, minute=0, second=0)
        self.timeslot1_end_time= datetime.time(hour=8, minute=50, second=0)
        self.lecture1_type= 0

        self.course1_name= 'Software Engineering'
        self.course1_code= 'cs305'

        #create Department Object
        self.department1= Department.objects.create(
            name= self.department_name1,
        )

        #create Faculty Object
        user_name1= 'Balwinder Sodhi'
        user_email1= 'sodhi@iitrpr.ac.in'
        self.user1= User.objects.create_user(
            username= user_name1, 
            email= user_email1,
            password= '',)
        self.faculty1= Faculty.objects.create(
            user= self.user1,
            department= self.department1,
        )

        #create timeslot object
        self.timeslot1= Timeslot.objects.create(
            name= self.timeslot1_name,
        )

        #create timeslot details object
        self.timeslot1_details= TimeSlotDetails.objects.create(
            timeslot= self.timeslot1,
            day= self.timeslot1_day,
            start_time= self.timeslot1_start_time,
            end_time= self.timeslot1_end_time,
            lecture_type= self.lecture1_type
        )

        #create course object
        self.course1= Course.objects.create(
            name= self.course1_name,
            code= self.course1_code,
            department= self.department1,
            course_coordinator= self.faculty1,
            timeslot= self.timeslot1
        )

    def test_department_str(self):
        self.assertEqual(self.department1.__str__(), self.department_name1,
            'Test Error in __str__() of Department model in courses app'
        )
    
    def test_timeslot_str(self):
        self.assertEqual(self.timeslot1.__str__(), self.timeslot1_name.upper(),
            'Test Error in __str__() of Timeslot model in courses app',
        )
    
    def test_timeslot_details_str(self):
        self.assertEqual(
            self.timeslot1_details.__str__(),
            self.timeslot1.__str__()+ ' '+ str(self.timeslot1_day)+ ' '+ str(self.timeslot1_start_time),
            'Test Error in __str__() of Timeslot_details model in courses app'
        )
    
    def test_courses_str(self):
        self.assertEqual(
            self.course1.__str__(),
            self.course1_code.upper()+ ' '+ self.course1_name,
            'Test Error in __str__() of Courses model in courses app'
        )