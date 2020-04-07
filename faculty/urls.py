from django.urls import path

from faculty import api

urlpatterns = [
    path('courses/', api.FacultyCourseList.as_view()),
]
