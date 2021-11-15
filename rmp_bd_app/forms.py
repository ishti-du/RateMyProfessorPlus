from django import forms


from .models import University, Department, Professor, StudentProfile, ProfessorProfile, Review, Course, ReviewTag
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
    # tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Review.objects.all())
    class Meta:
        model = Review
        fields = ['tags',  # 'course_number', 'course_title',
                  'grade', 'semester', 'year',
                  'mad_text', 'sad_text', 'glad_text',
                  'difficulty_level', 'professor_score', 'is_online', 'is_textbook',
                  'is_credit', 'addTag']
        labels = {
            # 'course_title': 'Course Title',
            # 'course_number': 'Course Code',
            'grade': 'Grade Received',
            'semester': 'Semester Taken',
            'year': 'Year Taken',
            'is_online': 'Online',
            'mad_text': 'Mad: (e.g., things that you wish were not there)',
            'sad_text': 'Sad: (e.g., things that you would change)',
            'glad_text': 'Glad: (e.g., things you will want to keep for future students)',
            'difficulty_level': 'Level of Difficulty',
            'professor_score': 'Rate Your Professor',
            'tags': 'Choose Your Tags',
            'is_online': 'Did you take this class online?',
            'is_textbook': 'Did you use the textbook(s) for this class?',
            'is_credit': 'Did you take this class for credit?',
            'addTag': 'Suggest New Tags'
        }

