from django.urls import path

from student import api

urlpatterns = [
    path('courses/', api.StudentCoursesList.as_view()),
]