"""Defines URL patterns for rmp_bd_app"""

from django.urls import path

from . import views
from django.contrib.auth import views as auth_views



app_name = 'rmp_bd_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # List of universities
    path('university/', views.universities, name='universities'),
    # List of campuses from a university
    path('university/<int:university_id>/campus', views.campuses, name='campuses'),
    # List of departments from a campus
    path('campus/<int:campus_id>/departments', views.departments, name='departments'),
    # Page for adding a new University
    path('new_university/', views.new_university, name='new_university'),
    # List of professors from a department
    path('department/<int:department_id>/professor', views.professor, name='professor'),
    
    path('professor_details/<int:professor_id>', views.professor_details, name='professor_details'),
    path('campus/<int:campus_id>/new_department/', views.new_department, name='new_department'),
    path('university/<int:university_id>/new_campus/', views.new_campus, name='new_campus'),

    # Page for adding a new professor
    path('department/<int:department_id>/new_professor', views.new_professor, name='new_professor'),
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
    # Course search autocomplete
    path('search_course/', views.search_course),
    # Profile update
    path('profile_update/', views.user_profile_update_view, name="profile_update"),
    # professor search results
    path('search/', views.SearchProfessorsResultsView.as_view(), name='search_results'),
    # password change
    path('change_password/', views.change_password, name = 'change_password')
]

