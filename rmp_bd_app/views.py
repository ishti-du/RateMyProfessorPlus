from django.shortcuts import render, redirect
from django.http import JsonResponse

<<<<<<< HEAD
from .models import University, Department, Faculty, Course
from .forms import UniversityForm, DepartmentForm, FacultyForm, FeedbackForm, CourseForm
=======
from .models import University, Department, Professor
from .forms import UniversityForm, DepartmentForm, FeedbackForm, ProfessorForm

>>>>>>> db31ddf2aac6fc385099bae7cfc960001ca6579c

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

<<<<<<< HEAD
def new_feedback(request):
    """Add a new Feedback"""
=======

def new_feedback(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
>>>>>>> db31ddf2aac6fc385099bae7cfc960001ca6579c
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
    context = {'form': form, 'professor': professor}
    return render(request, 'rmp_bd_app/reviewform.html', context)

def new_course(request):
    """Add a new course"""
    form = CourseForm() 
    course_query = Course.objects.all()
    courses = []
    for c in course_query:
        courses.append((c.course_number, c.course_title))
    context = {'form': form, 'courses': courses}
    if request.method == 'POST':
        # POST data submitted; process date_added
        # Redirects back to add course page
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:new_course', context)
            
    # Display a blank or invalid form
    return render(request, 'rmp_bd_app/new_course.html', context)

# /search/?course=
# Request made whenever input is made in course number
# Filters courses based on course number
def search_course(request):
    course_number = request.GET.get('course')
    course_numbers = []
    if course_number:
        courses = Course.objects.filter(course_number__icontains=course_number)
        for course in courses:
            course_numbers.append((course.course_number, course.course_title))
    return JsonResponse({'status': 200, 'data' : course_numbers})