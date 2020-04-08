from django.test import TestCase
from django.contrib.auth.models import User
from faculty.models import Faculty
from course.models import Department

class TestModels(TestCase):

    def setUp(self):
        user_name1= 'Balwinder Sodhi'
        user_email1= 'sodhi@iitrpr.ac.in'
        department_name1= 'Computer Science and Engineering'

        self.user1= User.objects.create_user(
            username= user_name1, 
            email= user_email1,
            password= '',)

        self.department1= Department.objects.create(
            name= department_name1,
        )

        self.faculty1= Faculty.objects.create(
            user= self.user1,
            department= self.department1,
        )


    def test_faculty_str(self):
        self.assertEqual(self.faculty1.__str__(), self.user1.__str__(), 'Error in __str__() of Faculty Class')