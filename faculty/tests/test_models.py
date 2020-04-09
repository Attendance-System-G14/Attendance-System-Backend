from django.test import TestCase
from django.contrib.auth.models import User
from faculty.models import Faculty
from course.models import Department

import objects_for_tests

class TestModels(TestCase):

    def setUp(self):
        objects_for_tests.variables()

    def test_faculty_str(self):
        self.assertEqual(objects_for_tests.faculty1.__str__(), 
                            objects_for_tests.faculty_user1.__str__(), 
                            'Error in __str__() of Faculty Class'
                        )