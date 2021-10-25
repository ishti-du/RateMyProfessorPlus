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
    # Page for adding a new faculty
    path('new_faculty/', views.new_faculty, name='new_faculty'),
    # Page for adding a new feedback
    path('new_feedback/<int:professor_id>', views.new_feedback, name='new_feedback'),
    # Test page for adding a course
    path('new_course/', views.new_course, name='new_course'),
    ]
