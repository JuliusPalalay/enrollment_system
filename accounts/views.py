from multiprocessing import AuthenticationError
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import StudentSignUpForm, EnrollmentForm
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Enrollment, Student, Subject
from .serializers import EnrollmentSerializer, StudentSerializer, SubjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status

# def student_signup(request):
#     if request.method == 'POST':
#         form = StudentSignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = StudentSignUpForm()
#     return render(request, 'registration/signup_form.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             form = AuthenticationError()
#             return render(request, 'registration/login.html', {'form': form})
#     else:/
#         form = AuthenticationForm()
#         return render(request, 'registration/login.html', {'form': form})
    
    
@csrf_exempt
def enrollment_list(request):
    """
    List all enrollments or create a new enrollment.
    """
    if request.method == 'GET':
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET'])
def accounts(request):
    """
    List all students or create a new student.
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE'])
def subject_view(request, pk=None):
    """
    Retrieve, create, or delete a subject instance.
    """
    if request.method == 'GET':
        if pk is None:
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
        else:
            try:
                subject = Subject.objects.get(pk=pk)
            except Subject.DoesNotExist:
                raise Http404
            serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404
        subject.delete()
        return JsonResponse({'detail': 'Deleted successfully'}, status=204)
    
# def enrollment_list(request):
#     enrollments = Enrollment.objects.all()
#     return render(request, 'enrollment_list', {'enrollments': enrollments})

# def enrollment_create(request):
#     if request.method == 'POST':
#         form = EnrollmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('enrollment_list')
#     else:
#         form = EnrollmentForm()
#     return render(request, 'enrollment_form', {'form': form})

# def enrollment_update(request, pk):
#     enrollment = Enrollment.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EnrollmentForm(request.POST, instance=enrollment)
#         if form.is_valid():
#             form.save()
#             return redirect('enrollment_list')
#     else:
#         form = EnrollmentForm(instance=enrollment)
#     return render(request, 'enrollment_form', {'form': form})

# def enrollment_delete(request, pk):
#     enrollment = Enrollment.objects.get(pk=pk)
#     if request.method == 'POST':
#         enrollment.delete()
#         return redirect('enrollment_list')
#     return render(request, 'enrollment_confirm_delete', {'enrollment': enrollment})