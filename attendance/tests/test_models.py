from django.test import TestCase
from datetime import datetime

import test_data.objects_for_tests as objects_for_tests

class TestModels(TestCase):

    def setUp(self):
        objects_for_tests.variables()

    def test_attendance_str_(self):
        self.assertEqual(
            objects_for_tests.attendance1.__str__(),
            objects_for_tests.course1_code.upper()+ ' '+ objects_for_tests.course1_name+ ' '+
                str(objects_for_tests.date_time1)+ ' '+ objects_for_tests.student_user1.__str__(),
            'Error in test for Attendance class in attendance app'
        )