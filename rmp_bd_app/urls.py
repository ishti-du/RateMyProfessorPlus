"""Defines URL patterns for rmp_bd_app"""

from django.urls import path

from . import views



app_name = 'rmp_bd_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # University
    path('university/', views.universities, name='universities'),
    path('university/<int:university_id>/departments', views.departments, name='departments'),
    # Page for adding a new University
    path('new_university/', views.new_university, name='new_university'),
    # Page for faculty listing
    path('professor/<int:department_id>', views.professor, name='professor'),
    path('professor_details/<int:professor_id>', views.professor_details, name='professor_details'),
    path('new_department/', views.new_department, name='new_department'),

    # Page for adding a new professor
    path('new_professor/', views.new_professor, name='new_professor'),
    # Page for adding a new review
    path('new_review/<int:professor_id>', views.new_review, name='new_review'),
    # Page for student sign up
    path('student_signup/', views.student_signup_view, name="student_signup"),
    # Page for professor sign up
    path('professor_signup/', views.professor_signup_view, name="professor_signup"),
    # Page for sign in
    path('login/', views.signin_view, name="signin"),
    # Page for sign out
    path('logout/', views.signout_view, name="signout"),

    path('profile/', views.user_profile_view, name="profile"),
    # Test page for adding a course
    path('new_course/', views.new_course, name='new_course'),
    path('new_tag/', views.new_tag, name='new_tag')
    ]
