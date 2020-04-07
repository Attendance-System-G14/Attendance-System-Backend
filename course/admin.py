from django.contrib import admin

from course import models

# Register your models here.

class CourseAdminView(admin.ModelAdmin):
    list_display = [field.name for field in models.Course._meta.fields]

admin.site.register(models.Course, CourseAdminView)

class DepartmentDeAdminView(admin.ModelAdmin):
    list_display = [field.name for field in models.Department._meta.fields]

admin.site.register(models.Department, DepartmentDeAdminView)