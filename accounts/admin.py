from django.contrib import admin
from .models import Student, College, Subject, Enrollment

admin.site.register(Student)
admin.site.register(College)
admin.site.register(Subject)
admin.site.register(Enrollment)