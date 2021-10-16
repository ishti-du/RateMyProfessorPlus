from django.shortcuts import render, redirect

from .forms import UniversityForm, DepartmentForm, FacultyForm, FeedbackForm
from .models import University, Department, Faculty, User
from django.db.models import Q


# Create your views here.
def index(request):
    """The home page for RMP BD"""

    ''' # Matt Coutts 10/18 --> import users to flag if student, prof, etc (later feature) '''
    student = User.ROLES[0]
    professor = User.ROLES[1]  # this is our professor user
    admin = User.ROLES[2]  # this is our admin user

    '''
    ~~~~~~~~~
    Matt Coutts - 10/16/2021 
    Here we are going to find the 'user/site visitors IP address to flag them. 
    This can be used with the thumbs up/down limit and comment limit
    '''

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED-FOR')
        if address:
            User.ip_address = address.split(',')[-1].strip()
        else:
            User.ip_address = request.META.get('REMOTE_ADDR')
        return User.ip_address

    User.ip_address = get_ip(request)

    result = User.ip_address

    #this determines if the IP address is repeated
    if len(result) == 1:
        print("user exists")
    elif len(result) > 1:
        print("duplicate IP user")
    else:
        User.ip_address.save()
        print('user IP is unique')

    count=User.objects.all().count()
    print("Total users are: ", count)

    # return the base html and page
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
    context = {'university': university, 'departments': departments}
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
    context = {'form': form}
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
    context = {'form': form}
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
    context = {'form': form}
    return render(request, 'rmp_bd_app/new_faculty.html', context)


def new_feedback(request):
    """Add a new Faculty"""
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
    context = {'form': form}
    return render(request, 'rmp_bd_app/new_feedback.html', context)
