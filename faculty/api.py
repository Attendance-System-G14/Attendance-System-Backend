from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from faculty.models import FacultyTakesCourse
from course.serializers import CourseSerializer

from faculty.permissions import IsFacultyUser

class FacultyCourseList(APIView):
    """
    View to list all courses of the faculty.

    * Requires token authentication.
    * Only faculty users are able to access this view.
    """
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsFacultyUser]

    def get(self, request, format=None):
        """
        Return Courses of the faculty
        """
        facultytakescourses = FacultyTakesCourse.objects.filter(faculty__user=request.user)
        courses = [facultytakescourse.course for facultytakescourse in facultytakescourses]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)