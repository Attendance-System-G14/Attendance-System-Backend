from rest_framework import serializers

from student.models import StudentTakesCourse
from course.serializers import CourseSerializer
from faculty.models import FacultyTakesCourse

class StudentCourseSerializer(serializers.Serializer):
    course = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    classess_total = serializers.SerializerMethodField()
    classess_present = serializers.SerializerMethodField()

    def get_course(self, instance):
        serilized_course = CourseSerializer(instance.course)
        return serilized_course.data

    def get_faculty(self, instance):
        try:
            faculty = FacultyTakesCourse.objects.get(course=instance.course).faculty
            return faculty.user.get_full_name()
        except FacultyTakesCourse.DoesNotExist:
            return 'not_assined'

    # Create some helper functions and change below
    def get_classess_total(self, instance):
        return 0

    def get_classess_present(self, instance):
        return 0