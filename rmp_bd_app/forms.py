from django import forms

from .models import University, Department, Faculty, Feedback, Course


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['country', 'university_name']
        labels = {'text': ''}


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['university', 'department_name']
        labels = {'text': ''}


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['department', 'faculty']
        labels = {'text': ''}


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['faculty', 'feedback']
        labels = {'text': ''}

# Temporary form to create class
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_title']
        labels = {'text': ''}