from django.urls import path
from . import views


urlpatterns = [
    # path('signup/', views.student_signup, name='signup'),
    # path('login/', views.login_view, name='login'),
    path('enrollments/', views.enrollment_list),
    path('student/', views.accounts),
    path('subjects/', views.subject_view, name='subject_list_create'),
    path('subjects/<int:pk>/', views.subject_view, name='subject_retrieve_delete'),
]
