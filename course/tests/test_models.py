from django.test import TestCase
from django.contrib.auth.models import User
from course.models import Department, Timeslot, TimeSlotDetails, Course
from faculty.models import Faculty
import datetime

import test_data.objects_for_tests as objects_for_tests

class TestModels(TestCase):

    def setUp(self):
        objects_for_tests.variables()

    def test_department_str(self):
        self.assertEqual(objects_for_tests.department1.__str__(), objects_for_tests.department_name1,
            'Test Error in __str__() of Department model in courses app'
        )
    
    def test_timeslot_str(self):
        self.assertEqual(objects_for_tests.timeslot1.__str__(), objects_for_tests.timeslot1_name.upper(),
            'Test Error in __str__() of Timeslot model in courses app',
        )
    
    def test_timeslot_details_str(self):
        self.assertEqual(
            objects_for_tests.timeslot1_details.__str__(),
            objects_for_tests.timeslot1.__str__()+ ' '+ str(objects_for_tests.timeslot1_day)+ 
                ' '+ str(objects_for_tests.timeslot1_start_time),
            'Test Error in __str__() of Timeslot_details model in courses app'
        )
    
    def test_courses_str(self):
        self.assertEqual(
            objects_for_tests.course1.__str__(),
            objects_for_tests.course1_code.upper()+ ' '+ objects_for_tests.course1_name,
            'Test Error in __str__() of Courses model in courses app'
        )