from django import forms


from .models import University, Department, Professor, StudentProfile, ProfessorProfile, Review, Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['current_university', 'campus', 'department', 'honorific', 'first_name', 'last_name']
        labels = {'text': ''}


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    username = forms.CharField(disabled=True)


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['university']


class ProfessorProfileForm(forms.ModelForm):

    class Meta:
        model = ProfessorProfile
        fields = ['faculty_directory_url', 'faculty_phone_number']

# Temporary form to create class
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_title']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['professor']
        labels = {'text': ''}