from rest_framework import permissions

from student.models import Student

class IsStudentUser(permissions.BasePermission):
    message= 'You are not a student member'

    def has_permission(self, request, view):
        # Identify if a user is a student
        try:
            Student.objects.get(user= request.user)
            return True
        except Student.DoesNotExist:
            return False