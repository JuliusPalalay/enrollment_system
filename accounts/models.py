from django.db import models
from django.contrib.auth.models import AbstractUser

class College(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    offer_code = models.CharField(max_length=255)
    course_number = models.CharField(max_length=255)
    descriptive_title = models.CharField(max_length=255)
    units = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.descriptive_title
    
class Student(AbstractUser):
    student_number = models.CharField(max_length=200, null=True)
    college = models.CharField(max_length=200)
    degree_program = models.CharField(max_length=200)
    year_level = models.IntegerField(default=1)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
