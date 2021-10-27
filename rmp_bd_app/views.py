from django.shortcuts import render, redirect
from .models import University, Department, Faculty
from .forms import UniversityForm, DepartmentForm, FacultyForm, FeedbackForm, StudentProfileForm, ProfessorProfileForm, CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ipware import get_client_ip

# Create your views here.
def index(request):
    """The home page for RMP BD"""
    print("is authenticated", request.user.is_authenticated, request.user)

    '''
    ~~~~~~~~~
    Matt Coutts - 10/16/2021 
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

    print(ip, ipv)



    return render(request, 'rmp_bd_app/index.html')

    return render(request, 'rmp_bd_app/index.html', {"user": request.user})



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


def student_signup_view(request):
    user_form = CreateUserForm(request.POST)
    student_form = StudentProfileForm(request.POST)
    if request.method == "POST":
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            profile = student_form.save(commit=False)
            profile.user = user
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
