"""Defines URL patterns for rmp_bd_app"""

from django.urls import path

from . import views

<<<<<<< HEAD


=======
>>>>>>> b4681ab27aa28cca18d0aeea0ac4d298e4bd1a30
app_name = 'rmp_bd_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # University
    path('university/', views.universities, name='universities'),
    path('university/<int:university_id>', views.university, name='university'),
    # Page for adding a new University
    path('new_university/', views.new_university, name='new_university'),
    # Page for faculty listing
    path('faculties/<int:department_id>', views.faculty, name='faculty'),
    # Page for individual faculty feeback
    path('faculty_details/<int:faculty_id>', views.faculty_details, name='faculty_details'),
    # Page for adding a new department
    path('new_department/', views.new_department, name='new_department'),
    # Page for adding a new faculty
    path('new_faculty/', views.new_faculty, name='new_faculty'),
    # Page for adding a new feedback
    path('new_feedback/', views.new_feedback, name='new_feedback'),
    # Page for student sign up
    path('student_signup/', views.student_signup_view, name="student_signup"),
    # Page for professor sign up
    path('professor_signup/', views.professor_signup_view, name="professor_signup"),
    # Page for sign in
    path('login/', views.signin_view, name="signin"),
    # Page for sign out
    path('logout/', views.signout_view, name="signout")
    ]
