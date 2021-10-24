from django import forms


from .models import University, Department, Faculty, Feedback, Student_Profile, Professor_Profile
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


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['faculty', 'feedback']
        labels = {'text': ''}


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = Student_Profile
        fields = ['school_name']


class ProfessorProfileForm(forms.ModelForm):

    class Meta:
        model = Professor_Profile
        fields = ['faculty_directory_url', 'faculty_phone_number']