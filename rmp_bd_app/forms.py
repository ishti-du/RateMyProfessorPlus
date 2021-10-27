from django import forms

from .models import University, Department, Feedback, Professor, Review


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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['grade', 'semester', 'year', 'is_online',
                  'mad_text', 'sad_text', 'glad_text']
        #fields = ['grade', 'mad_text', 'sad_text', 'glad_text',
        #          'semester', 'year']
        #labels = {'text': ''}

class ReviewForm1(forms.Form):
    grade = forms.CharField()
    semester = forms.CharField(widget="")
        #labels = {'text': ''}