from rest_framework.serializers import ModelSerializer
from .models import  Student, College, Subject,Enrollment

class StudentSerializer(ModelSerializer):
    class Meta:
        model =  Student
        fields = '__all__'


class CollegeSerializer(ModelSerializer):
    class Meta:
        model =  College
        fields = '__all__'

class SubjectSerializer(ModelSerializer):
    class Meta:
        model =  Subject
        fields = '__all__'


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model =  Enrollment
        fields = '__all__'