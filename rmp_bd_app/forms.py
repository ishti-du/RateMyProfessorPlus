from django import forms

from .models import University, Department, Faculty, Feedback, Student_Profile
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

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


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = Student_Profile
        fields = ['school_name']