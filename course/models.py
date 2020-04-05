from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.code + ' ' + self.name