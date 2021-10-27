from django.shortcuts import render, redirect

from .models import University, Department, Professor
from .forms import UniversityForm, DepartmentForm, FeedbackForm, ProfessorForm, ReviewForm


# Create your views here.
def index(request):
    """The home page for RMP BD"""
    return render(request, 'rmp_bd_app/index.html')

def universities(request):
    """The univeristy page for RMP BD"""
    universities = University.objects.order_by('date_added')
    context = {'universities': universities}
    return render(request, 'rmp_bd_app/universities.html', context)

def departments(request, university_id):
    university = University.objects.get(id=university_id)
    departments = Department.objects.filter(university=University.objects.get(id=university_id)).order_by('date_added')
    context = {'departments': departments, 'university': university}
    return render(request, 'rmp_bd_app/departments.html', context)

def university(request, university_id):
    """Shows each individual university """
    university = University.objects.get(id=university_id)
    departments = university.department_set.order_by('-date_added')
    context = {'university' : university, 'departments' : departments}
    return render(request, 'rmp_bd_app/universities.html', context)

def professor(request, department_id):
    """Shows faculty members for a department"""
    department = Department.objects.get(id=department_id)
    professor = Professor.objects.filter(department=Department.objects.get(id=department_id)).order_by('date_added')
    context = {'department': department, 'professor': professor}
    return render(request, 'rmp_bd_app/professors.html', context)

def professor_details(request, professor_id):
    """Shows the students' feedback about a faculty"""
    professor = Professor.objects.get(id=professor_id)
    #feedback = faculty.feedback_set.order_by('-date_added')
    context = {'professor': professor}
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
        form = ProfessorForm()
    else:
        # POST data submitted; process date_added
        form = ProfessorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:universities')

    # Display a blank or invalid form
    context  = {'form': form}
    return render(request, 'rmp_bd_app/new_faculty.html', context)


def new_feedback(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = ReviewForm()
    else:
        # POST data submitted; process date_added
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:universities')

    # Display a blank or invalid form
    context = {'form': form, 'professor': professor}
    return render(request, 'rmp_bd_app/reviewform.html', context)

def new_feedback1(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    if request.method == 'POST':
        code = request.POST['code']
        ctite = request.POST['ctitle']


    # Display a blank or invalid form
    context = {'form': form, 'professor': professor}
    return render(request, 'rmp_bd_app/reviewform.html', context)

    
