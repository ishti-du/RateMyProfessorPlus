from django.shortcuts import render, redirect

from .models import University, Department, Faculty, Professor
from .forms import UniversityForm, DepartmentForm, FacultyForm, FeedbackForm

# Create your views here.
def index(request):
    """The home page for RMP BD"""
    return render(request, 'rmp_bd_app/index.html')

def universities(request):
    """The univeristy page for RMP BD"""
    universities = University.objects.order_by('date_added')
    context = {'universities': universities}
    return render(request, 'rmp_bd_app/universities.html', context)

def departments(request):
    """The departments page for RMP BD"""
    departments = Department.objects.order_by('date_added')
    context = {'Departments': departments}
    return render(request, 'rmp_bd_app/departments.html', context)

def university(request, university_id):
    """Shows each individual university """
    university = University.objects.get(id=university_id)
    departments = university.department_set.order_by('-date_added')
    context = {'university' : university, 'departments' : departments}
    return render(request, 'rmp_bd_app/departments.html', context)

def professor(request, department_id):
    """Shows faculty members for a department"""
    department = Department.objects.get(id=department_id)
    professor = department.faculty_set.order_by('-date_added')
    context = {'department': department, 'faculties': professor}
    return render(request, 'rmp_bd_app/professsors.html', context)

def professor_details(request, faculty_id):
    """Shows the students' feedback about a faculty"""
    professor = Professor.objects.get(id=faculty_id)
    #feedback = faculty.feedback_set.order_by('-date_added')
    context = {'Professor': professor,}
    return render(request, 'rmp_bd_app/professor_details.html', context)

def new_university(request):
    """Add a new University"""
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = UniversityForm()
    else:
        # POST data submitted; process date_added
        form = UniversityForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:universities')

    # Display a blank or invalid form
    context  = {'form': form}
    return render(request, 'rmp_bd_app/new_university.html', context)

def new_department(request):
    """Add a new Department"""
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = DepartmentForm()
    else:
        # POST data submitted; process date_added
        form = DepartmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:universities')

    # Display a blank or invalid form
    context  = {'form': form}
    return render(request, 'rmp_bd_app/new_department.html', context)

def new_faculty(request):
    """Add a new Faculty"""
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = FacultyForm()
    else:
        # POST data submitted; process date_added
        form = FacultyForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:universities')

    # Display a blank or invalid form
    context  = {'form': form}
    return render(request, 'rmp_bd_app/new_faculty.html', context)


def new_feedback(request, faculty_id):
    professor = Professor.objects.get(id=faculty_id)
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = FeedbackForm()
    else:
        # POST data submitted; process date_added
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:universities')

    # Display a blank or invalid form
    context = {'form': form, 'Professor': professor}
    return render(request, 'rmp_bd_app/reviewform.html', context)

    
