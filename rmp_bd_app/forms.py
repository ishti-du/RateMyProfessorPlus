from django import forms

from .models import University, Department, Feedback, Professor, Course


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

# Temporary form to create class
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_title']
        labels = {'text': ''}