from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models.fields import PositiveBigIntegerField
from django.http import JsonResponse, request
from django.shortcuts import redirect, render
from ipware import get_client_ip  # this package retrieves the clients IP

from .forms import (CourseForm, CreateUserForm, DepartmentForm, FeedbackForm,
                    ProfessorForm, ProfessorProfileForm, StudentProfileForm,
                    UniversityForm)
from .models import Course, Department, Professor, Professor_Profile, Student_Profile, University

''' Func that retrieves the IP address at the start of the website '''
def retrieveIP(request): 
    '''
    ~~~~~
    Matt Coutts - 11/01/2021 
    Here we are going to find the 'user/site visitors IP address to flag them. 
    This can be used with the thumbs up/down limit and comment limit
    Reference: https://www.youtube.com/watch?v=cbMLP3byKjk 
    '''
    ip, is_routable = get_client_ip(request)

    # if we can't get the IP then we check constraints here
    if ip is None:
        ip = "0.0.0.0" # set IP as 0.0.0.0 if we can't find it
    else:
        # routable = True or False
        if is_routable:
            ipv = "Public" # if the ip returns true (not local)
        else:
            ipv = "Private" # if the ip returns false (local)

    try:
        Student_Profile.ip_address = ip
        
    except: 
        print("Error in models.py IPProfile Capture") 

        print(ip)
        return(ip)


# this function adds the IP to the speocific profile based on the type of profile signed in, i hope 
def IPProfileCapture(request):
    pass

# Create your views here.
def index(request):
    """The home page for RMP BD"""

    ip = retrieveIP(request) # retrieving the IP
    
    print("is authenticated", request.user.is_authenticated, request.user)
    Student_Profile.ip_address = ip
    Professor_Profile.ip_address = ip
    return render(request, 'rmp_bd_app/index.html', {"user": request.user})


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
        form = ProfessorForm()
    else:
        # POST data submitted; process date_added
        form = ProfessorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:universities')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'rmp_bd_app/new_faculty.html', context)


def new_feedback(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
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

def student_signup_view(request):
    user_form = CreateUserForm(request.POST)
    student_form = StudentProfileForm(request.POST)
    if request.method == "POST":
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            profile = student_form.save(commit=False)
            profile.user = user
            profile.ipaddress = "0.0.0.0"
            profile.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    return render(request, 'rmp_bd_app/student_signup.html', {'user_form': user_form, 'student_form': student_form})

def professor_signup_view(request):
    user_form = CreateUserForm(request.POST)
    professor_form = ProfessorProfileForm(request.POST)
    if request.method == "POST":
        if user_form.is_valid() and professor_form.is_valid():
            user = user_form.save()
            profile = professor_form.save(commit=False)
            profile.user = user
            profile.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    return render(request, 'rmp_bd_app/professor_signup.html', {'user_form': user_form, 'professor_form': professor_form})

def signin_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'rmp_bd_app/login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                print(user)
                login(request, user)
                return redirect('/')
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'rmp_bd_app/login.html', {'form': form})


def signout_view(request):
    logout(request)
    return redirect('/login')


def user_profile_view(request):
    return render(request, 'rmp_bd_app/profile.html')

def signedIn():
    user = authenticate(True)
    if user is not None: 
        return user