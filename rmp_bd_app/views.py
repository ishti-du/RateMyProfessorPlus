from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import University, Department, Faculty, Course
from .forms import UniversityForm, DepartmentForm, FacultyForm, FeedbackForm, CourseForm

# Create your views here.
def index(request):
    """The home page for RMP BD"""
    return render(request, 'rmp_bd_app/index.html')

def universities(request):
    """The univeristy page for RMP BD"""
    universities = University.objects.order_by('date_added')
    context = {'universities': universities}
    return render(request, 'rmp_bd_app/universities.html', context)

def university(request, university_id):
    """Shows each individual university """
    university = University.objects.get(id=university_id)
    departments = university.department_set.order_by('-date_added')
    context = {'university' : university, 'departments' : departments}
    return render(request, 'rmp_bd_app/departments.html', context)

def faculty(request, department_id):
    """Shows faculty members for a department"""
    department = Department.objects.get(id=department_id)
    faculties = department.faculty_set.order_by('-date_added')
    context = {'department': department, 'faculties': faculties}
    return render(request, 'rmp_bd_app/faculties.html', context)

def faculty_details(request, faculty_id):
    """Shows the students' feedback about a faculty"""
    faculty = Faculty.objects.get(id=faculty_id)
    feedback = faculty.feedback_set.order_by('-date_added')
    context = {'faculty': faculty, 'feedback': feedback}
    return render(request, 'rmp_bd_app/faculty_details.html', context)

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

def new_feedback(request):
    """Add a new Feedback"""
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
    context  = {'form': form}
    return render(request, 'rmp_bd_app/new_feedback.html', context)

def new_course(request):
    """Add a new course"""
    form = CourseForm() 
    courses = Course.objects.all
    context = {'form': form, 'courses': courses}
    if request.method == 'POST':
        # POST data submitted; process date_added
        # Redirects back to add course page
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:new_course', context)
            
    # Display a blank or invalid form
    context = {'form': form, 'courses': courses}
    return render(request, 'rmp_bd_app/new_course.html', context)

# /search/?course=
def search_course(request):
    course_number = request.GET.get('course')
    course_numbers = []
    if course_number:
        courses = Course.objects.filter(course_number__icontains=course_number)
        for course in courses:
            course_numbers.append((course.course_number, course.course_title))

    return JsonResponse({'status': 200, 'data' : course_numbers})