from django.contrib import admin

from course import models

# Register your models here.

class CourseAdminView(admin.ModelAdmin):
    list_display = [field.name for field in models.Course._meta.fields]

admin.site.register(models.Course, CourseAdminView)

class DepartmentAdminView(admin.ModelAdmin):
    list_display = [field.name for field in models.Department._meta.fields]

admin.site.register(models.Department, DepartmentAdminView)

class TimeSlotAdminView(admin.ModelAdmin):
    list_display = [field.name for field in models.Timeslot._meta.fields]

admin.site.register(models.Timeslot, TimeSlotAdminView)

class TimeSlotDetailsAdminView(admin.ModelAdmin):
    list_display = [field.name for field in models.TimeSlotDetails._meta.fields]

admin.site.register(models.TimeSlotDetails, TimeSlotDetailsAdminView)