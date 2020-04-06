from django.db import models
from django.contrib.auth.models import User

from course.models import Department

# Create your models here.

class Faculty(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.__str__()