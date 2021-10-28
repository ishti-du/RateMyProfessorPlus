from django import forms


from .models import University, Department, Professor, Feedback, Student_Profile, Professor_Profile, Review
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

class ReviewForm(forms.ModelForm):
    #tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Review.objects.all())
    class Meta:
        model = Review
        fields = ['course',
                  'grade', 'semester', 'year',
                  'mad_text', 'sad_text', 'glad_text', 'tags',
                  'difficulty_level', 'professor_score', 'is_online', 'is_textbook',
                  'is_credit',]
        labels = {
            'course': 'Course Title',
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
        }
        widgets = {
            #'course': forms.TextInput(attrs={'class':'form-control'}),
            #'grade': forms.TextInput(attrs={'class':'form-control'}),
            #'mad_text': forms.Textarea(),
            #'tags': forms.CheckboxSelectMultiple()
            #slider!!!!! 'professor_score': forms.NumberInput(attrs={'type': 'range',  'min': '1', 'max': '5', 'value': '3', 'id': 'id_name'})
        }
