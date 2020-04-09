from django.contrib.auth.models import User
from student.models import Student
from faculty.models import Faculty
from course.models import Course, Department, Timeslot, TimeSlotDetails
import datetime

def variables():
    #create a user to be used as student
    global student_user1_name
    student_user1_name= 'Adarsh Kumar'
    global student_user1_email
    student_user1_email= '2017csb1064@iitrpr.ac.in'
    global student_user1_password
    student_user1_password= ''

    global student_user1
    student_user1= User.objects.create_user(
        username= student_user1_name,
        email= student_user1_email,
        password= student_user1_password,
    )

    #create a user to be used as a faculty
    global faculty_user1_name
    faculty_user1_name= 'Balwinder Sodhi'
    global faculty_user1_email
    faculty_user1_email= 'sodhi@iitrpr.ac.in'
    global faculty_user1_password
    faculty_user1_password= ''

    global faculty_user1
    faculty_user1= User.objects.create_user(
        username= faculty_user1_name,
        email= faculty_user1_email,
        password= faculty_user1_password,
    )

    #create Department Object
    global department_name1
    department_name1= 'Computer Science and Engineering'

    global department1
    department1= Department.objects.create(
        name= department_name1,
    )

    #create timeslot object
    global timeslot1_name
    timeslot1_name= 'a'
    global timeslot1
    timeslot1= Timeslot.objects.create(
        name= timeslot1_name,
    )

    #create timeslot details object
    global timeslot1_day
    timeslot1_day= 1
    global timeslot1_start_time
    timeslot1_start_time= datetime.time(hour=8, minute=0, second=0)
    global timeslot1_end_time
    timeslot1_end_time= datetime.time(hour=8, minute=50, second=0)
    global lecture1_type
    lecture1_type= 0
    global timeslot1_details
    timeslot1_details= TimeSlotDetails.objects.create(
        timeslot= timeslot1,
        day= timeslot1_day,
        start_time= timeslot1_start_time,
        end_time= timeslot1_end_time,
        lecture_type= lecture1_type
    )

    #create student object
    global student1_entry_number
    student1_entry_number= '2017csb1064'
    global student1
    student1= Student.objects.create(
        user= student_user1,
        entry_number= student1_entry_number,
        department= department1,
    )

    #create faculty object
    global faculty1
    faculty1= Faculty.objects.create(
        user= faculty_user1,
        department= department1,
    )

    #create course object
    global course1_name
    course1_name= 'Software Engineering'
    global course1_code
    course1_code= 'cs305'

    global course1
    course1= Course.objects.create(
        name= course1_name,
        code= course1_code,
        department= department1,
        course_coordinator= faculty1,
        timeslot= timeslot1
    )


if __name__ == "__main__":
    variables()