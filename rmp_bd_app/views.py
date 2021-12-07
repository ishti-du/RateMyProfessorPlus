from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic.list import ListView
from .models import University, Department, Professor, Course, User, StudentProfile, Campus
from .forms import UniversityForm, DepartmentForm, ProfessorForm, ReviewForm, StudentProfileForm, ProfessorProfileForm, CreateUserForm, CourseForm, CampusForm, UpdateUserForm, UpdateStudentProfileForm, UpdateProfessorProfileForm
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2


# Create your views here.
def index(request):
    """The home page for RMP BD"""
    print("is authenticated", request.user.is_authenticated, request.user)
    return render(request, 'rmp_bd_app/index.html', {"user": request.user})
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
        ip = "0.0.0.0"  # set IP as 0.0.0.0 if we can't find it
    else:
        # routable = True or False
        if is_routable:
            ipv = "Public"  # if the ip returns true (not local)
        else:
            ipv = "Private"  # if the ip returns false (local)

    print(ip, ipv)


def universities(request):
    """The univeristy page for RMP BD"""
    universities = University.objects.order_by('date_added')
    context = {'universities': universities}
    return render(request, 'rmp_bd_app/universities.html', context)


def departments(request, campus_id):
    campus = Campus.objects.get(id=campus_id)
    # university = University.objects.get(id=university_id)
    departments = Department.objects.filter(campus=campus).order_by('date_added')
    context = {'departments': departments, 'campus': campus}
    return render(request, 'rmp_bd_app/departments.html', context)


def campuses(request, university_id):
    university = University.objects.get(id=university_id)
    campuses = Campus.objects.filter(university=university).order_by('date_added')
    context = {'campuses': campuses, 'university': university}
    return render(request, 'rmp_bd_app/campuses.html', context)


def university(request, university_id):
    """Shows each individual university """
    university = University.objects.get(id=university_id)
    departments = university.department_set.order_by('-date_added')
    context = {'university': university, 'departments': departments}
    return render(request, 'rmp_bd_app/universities.html', context)


def professor(request, department_id):
    """Shows professors for a department"""
    department = Department.objects.get(id=department_id)
    professor = Professor.objects.filter(
        department=Department.objects.get(id=department_id)).order_by('date_added')
    context = {'department': department, 'professor': professor}
    return render(request, 'rmp_bd_app/professors.html', context)


def professor_details(request, professor_id):
    """Shows the students' reviews about a professor"""
    professor = Professor.objects.get(id=professor_id)
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


def new_department(request, campus_id):
    """Add a new Department"""
    campus = Campus.objects.get(id=campus_id)
    university = University.objects.get(id=campus.university.id)
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = DepartmentForm(initial={'university': university, 'campus': campus})
    else:
        # POST data submitted; process date_added
        form = DepartmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('rmp_bd_app:departments', kwargs={'campus_id': campus_id}))

    # Display a blank or invalid form
    context = {'form': form, 'campus': campus}
    return render(request, 'rmp_bd_app/new_department.html', context)


def new_campus(request, university_id):
    """Add a new Campus"""
    university = University.objects.get(id=university_id)
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = CampusForm(initial={'university': university})
    else:
        # POST data submitted; process date_added
        form = CampusForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse('rmp_bd_app:campuses', kwargs={'university_id': university_id}))

    # Display a blank or invalid form

    context = {'form': form, 'university': university}
    return render(request, 'rmp_bd_app/new_campus.html', context)


def new_professor(request):
    """Add a new Professor"""
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = ProfessorForm()
    else:
        # POST data submitted; process date_added
        form = ProfessorForm(data=request.POST)
        if form.is_valid():
            form.save()
            professor = Professor.objects.latest('id')
            context = {'professor': professor}
            return render(request, 'rmp_bd_app/professor_details.html', context)

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'rmp_bd_app/new_professor.html', context)


def new_review(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    if request.method != 'POST':
        # no data submitted, create a blank forms
        form = ReviewForm()
    else:
        # POST data submitted; process date_added
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rmp_bd_app:professor_details.html')

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

# /search/?university=&?course=
# Request made whenever input is made in course number


def search_course(request):
    request_dict = request.GET
    course_number = request_dict.get('course')
    university = request_dict.get('university')
    course_numbers = []
    if course_number:
        courses = Course.objects.filter(
            course_number__icontains=course_number
        ).filter(
            course_university__university_name=university
        )
        for course in courses:
            course_numbers.append((course.course_number, course.course_title))
    return JsonResponse({'status': 200, 'data': course_numbers})


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


def user_profile_view(request):
    return render(request, 'rmp_bd_app/profile.html', {"is_student": hasattr(request.user, 'student_profile'),
                                                       "is_professor": hasattr(request.user, 'professor_profile')})


def user_profile_update_view(request):
    if hasattr(request.user, 'student_profile'):
        ProfileForm = UpdateStudentProfileForm
        profile = request.user.student_profile
    elif hasattr(request.user, 'professor_profile'):
        ProfileForm = UpdateProfessorProfileForm
        profile = request.user.professor_profile
    else:
        ProfileForm = None
        profile = None
    profile_update_form = None

    if request.method == 'POST':
        print('###', request)
        user_update_form = UpdateUserForm(request.POST, instance=request.user)
        if user_update_form.is_valid():
            if ProfileForm is not None:
                profile_update_form = ProfileForm(
                    request.POST, instance=profile)
                if profile_update_form.is_valid():
                    print("I AM HERE")
                    profile_update_form.save()
                    user_update_form.save()
            else:
                user_update_form.save()
            return redirect('/profile')
    else:
        user_update_form = UpdateUserForm(instance=request.user)
        if ProfileForm:
            profile_update_form = ProfileForm(instance=profile)

    return render(request, 'rmp_bd_app/profile_update.html', {'user_update_form': user_update_form,
                                                              'profile_update_form': profile_update_form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'rmp_bd_app/change_password.html', {'form': form})


''' 
Creator: Mis Champa        Branch: Multicountry 2
/search/?q=Professor name
Request made whenever User will search any professor name
collect countyry database from maxmind company. Here is the link bellow
https://www.maxmind.com/en/geoip2-country-database
 '''
# Create SearchResultView function to filter Professor name based on IP address


class SearchProfessorsResultsView(ListView):
    model = Professor
    template_name = 'rmp_bd_app/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_globally = self.request.GET.getlist('search globally')

        # if user click checkbox, engine will search professor first and last name by globally
        if 'search globally' in search_globally:
            professor_list = Professor.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query))
        # checks if the user is authenticated
        elif self.request.user.is_authenticated:
            current_user = User.objects.get(id=self.request.user.id)
            user_profile = StudentProfile.objects.get(user_id=current_user.id)
            # getting user ip address
            user_ip = user_profile.ip_address
            # if user ip address is "0.0.0.0" ----> search by first or last name
            if user_ip == "0.0.0.0":
                professor_list = Professor.objects.filter(
                    Q(first_name__icontains=query) | Q(last_name__icontains=query))
            # if user ip address is not "0.0.0.0" ----> search by first or last name in the associated country
            else:
                g = GeoIP2()
                country = g.country_code(user_ip)
                professor_list = Professor.objects.filter(
                    (Q(first_name__icontains=query) |
                     Q(last_name__icontains=query)),
                    current_university__country=country
                )
        else:
            professor_list = Professor.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query))

        return professor_list
