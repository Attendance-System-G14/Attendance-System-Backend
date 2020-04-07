from rest_framework import permissions

from faculty.models import Faculty

class IsFacultyUser(permissions.BasePermission):
    message = 'You are not a faculty member.'

    def has_permission(self, request, view):
        # Identify if user is a faculty
        try:
            Faculty.objects.get(user=request.user)
            return True
        except Faculty.DoesNotExist:
            return False