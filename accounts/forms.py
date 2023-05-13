from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'student_number', 'college', 'degree_program', 'year_level',)
