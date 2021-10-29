[33mcommit 2137d65d8cd1f936c553c18b5de624628f2d113a[m[33m ([m[1;36mHEAD -> [m[1;32mcourseTitle[m[33m, [m[1;31morigin/courseTitle[m[33m)[m
Author: ChrisCee2 <chrischung411@gmail.com>
Date:   Sun Oct 17 01:03:21 2021 -0400

    Created page to add courses. Working on autocomplete

[1mdiff --git a/rmp_bd_app/forms.py b/rmp_bd_app/forms.py[m
[1mindex 0b31399..4e0293c 100644[m
[1m--- a/rmp_bd_app/forms.py[m
[1m+++ b/rmp_bd_app/forms.py[m
[36m@@ -1,6 +1,6 @@[m
 from django import forms[m
 [m
[31m-from .models import University, Department, Faculty, Feedback[m
[32m+[m[32mfrom .models import University, Department, Faculty, Feedback, Course[m
 [m
 [m
 class UniversityForm(forms.ModelForm):[m
[36m@@ -28,4 +28,11 @@[m [mclass FeedbackForm(forms.ModelForm):[m
     class Meta:[m
         model = Feedback[m
         fields = ['faculty', 'feedback'][m
[32m+[m[32m        labels = {'text': ''}[m
[32m+[m
[32m+[m[32m# Temporary form to create class[m
[32m+[m[32mclass CourseForm(forms.ModelForm):[m
[32m+[m[32m    class Meta:[m
[32m+[m[32m        model = Course[m
[32m+[m[32m        fields = ['course_number', 'course_title'][m
         labels = {'text': ''}[m
\ No newline at end of file[m
[1mdiff --git a/rmp_bd_app/templates/rmp_bd_app/base.html b/rmp_bd_app/templates/rmp_bd_app/base.html[m
[1mindex 7aeaeab..a08b2d6 100644[m
[1m--- a/rmp_bd_app/templates/rmp_bd_app/base.html[m
[1m+++ b/rmp_bd_app/templates/rmp_bd_app/base.html[m
[36m@@ -1,6 +1,7 @@[m
 <p>[m
   <a href="{% url 'rmp_bd_app:index' %}"> RateMyProfessor-BD</a> -[m
[31m-  <a href="{% url 'rmp_bd_app:universities' %}"> Universities </a>[m
[32m+[m[32m  <a href="{% url 'rmp_bd_app:universities' %}"> Universities </a> -[m
[32m+[m[32m  <a href="{% url 'rmp_bd_app:new_course' %}"> Add a new course </a>[m
 </p>[m
 [m
 {% block content %} {% endblock content%}[m
[1mdiff --git a/rmp_bd_app/templates/rmp_bd_app/new_course.html b/rmp_bd_app/templates/rmp_bd_app/new_course.html[m
[1mnew file mode 100644[m
[1mindex 0000000..9795867[m
[1m--- /dev/null[m
[1m+++ b/rmp_bd_app/templates/rmp_bd_app/new_course.html[m
[36m@@ -0,0 +1,58 @@[m
[32m+[m[32m{% block content %}[m
[32m+[m
[32m+[m[32m  <p>Courses</p>[m
[32m+[m[32m<ul>[m
[32m+[m[32m  {% for course in courses %}[m
[32m+[m[32m    <li>[m
[32m+[m[32m      <p>{{ course }}</p>[m
[32m+[m[32m    </li>[m
[32m+[m[32m  {% empty %}[m
[32m+[m[32m    <li>No topics have been added yet.</li>[m
[32m+[m[32m  {% endfor %}[m
[32m+[m[32m</ul>[m
[32m+[m[41m  [m
[32m+[m[32m  <p>Add a new Course:</p>[m
[32m+[m
[32m+[m[32m  <form action="{% url 'rmp_bd_app:new_course' %}" method="post">[m
[32m+[m[32m    {% csrf_token %}[m
[32m+[m[32m    {{ form.non_field_errors }}[m
[32m+[m[32m    <div style="display:flex;" id="autocomplete" class="autocomplete">[m
[32m+[m[32m      <div class="fieldWrapper" style="padding:5px;">[m
[32m+[m[32m        {{ form.course_number.errors }}[m
[32m+[m[32m        <label for="{{ form.course_number.id_for_label }}">[m
[32m+[m[32m          Course Number:[m
[32m+[m[32m          <br>[m
[32m+[m[32m          <input type="text" id="id_course_number" name="course_number" maxlength="10" class="autocomplete-input" required />[m
[32m+[m[32m        </label>[m
[32m+[m[32m      </div>[m
[32m+[m[32m      <div class="fieldWrapper" style="padding:5px;">[m
[32m+[m[32m        {{ form.course_title.errors }}[m
[32m+[m[32m        <label for="{{ form.course_title.id_for_label }}">[m
[32m+[m[32m          Course Title:[m
[32m+[m[32m          <br>[m
[32m+[m[32m          <input type="text" id="id_course_title" name="course_title" required>[m
[32m+[m[32m          <ul class="autocomplete-result-list"></ul>[m
[32m+[m[32m        </label>[m
[32m+[m[32m      </div>[m
[32m+[m[32m    </div>[m
[32m+[m[32m    <button name="submit">Add Course</button>[m
[32m+[m[32m  </form>[m
[32m+[m
[32m+[m[32m  <!-- Script for autocomplete -->[m
[32m+[m[32m  <script src="https://unpkg.com/@trevoreyre/autocomplete-js"></script>[m
[32m+[m[32m  <script>[m
[32m+[m[32m    new Autocomplete('#autocomplete', {[m
[32m+[m[32m      search : input => {[m
[32m+[m[32m        const url = `/search_course/?course=${input}`[m
[32m+[m[32m        return new Promise(resolve =>{[m
[32m+[m[32m          fetch(url)[m
[32m+[m[32m          .then(response => response.json())[m
[32m+[m[32m          .then(data => {[m
[32m+[m[32m            resolve(data.data)[m
[32m+[m[32m          })[m
[32m+[m[32m        })[m
[32m+[m[32m      },[m
[32m+[m[32m      autoselect: true[m
[32m+[m[32m    })[m
[32m+[m[32m  </script>[m
[32m+[m[32m{% endblock content %}[m
\ No newline at end of file[m
[1mdiff --git a/rmp_bd_app/urls.py b/rmp_bd_app/urls.py[m
[1mindex a3efa06..e46daa5 100644[m
[1m--- a/rmp_bd_app/urls.py[m
[1m+++ b/rmp_bd_app/urls.py[m
[36m@@ -23,5 +23,7 @@[m [murlpatterns = [[m
     # Page for adding a new faculty[m
     path('new_faculty/', views.new_faculty, name='new_faculty'),[m
     # Page for adding a new feedback[m
[31m-    path('new_feedback/', views.new_feedback, name='new_feedback')[m
[32m+[m[32m    path('new_feedback/', views.new_feedback, name='new_feedback'),[m
[32m+[m[32m    # Test page for adding a course[m
[32m+[m[32m    path('new_course/', views.new_course, name='new_course'),[m
     ][m
[1mdiff --git a/rmp_bd_app/views.py b/rmp_bd_app/views.py[m
[1mindex f93fa08..f1dd0df 100644[m
[1m--- a/rmp_bd_app/views.py[m
[1m+++ b/rmp_bd_app/views.py[m
[36m@@ -1,7 +1,8 @@[m
 from django.shortcuts import render, redirect[m
[32m+[m[32mfrom django.http import JsonResponse[m
 [m
[31m-from .models import University, Department, Faculty[m
[31m-from .forms import UniversityForm, DepartmentForm, FacultyForm, FeedbackForm[m
[32m+[m[32mfrom .models import University, Department, Faculty, Course[m
[32m+[m[32mfrom .forms import UniversityForm, DepartmentForm, FacultyForm, FeedbackForm, CourseForm[m
 [m
 # Create your views here.[m
 def index(request):[m
[36m@@ -83,9 +84,8 @@[m [mdef new_faculty(request):[m
     context  = {'form': form}[m
     return render(request, 'rmp_bd_app/new_faculty.html', context)[m
 [m
[31m-[m
 def new_feedback(request):[m
[31m-    """Add a new Faculty"""[m
[32m+[m[32m    """Add a new Feedback"""[m
     if request.method != 'POST':[m
         # no data submitted, create a blank forms[m
         form = FeedbackForm()[m
[36m@@ -100,4 +100,31 @@[m [mdef new_feedback(request):[m
     context  = {'form': form}[m
     return render(request, 'rmp_bd_app/new_feedback.html', context)[m
 [m
[31m-    [m
[32m+[m[32mdef new_course(request):[m
[32m+[m[32m    """Add a new course"""[m
[32m+[m[32m    if request.method != 'POST':[m
[32m+[m[32m        courses = Course.objects.all[m
[32m+[m[32m        # no data submitted, create a blank form[m
[32m+[m[32m        form = CourseForm()[m[41m [m
[32m+[m[32m    else:[m
[32m+[m[32m        # POST data submitted; process date_added[m
[32m+[m[32m        # Redirects back to add course page[m
[32m+[m[32m        form = CourseForm(data=request.POST)[m
[32m+[m[32m        if form.is_valid():[m
[32m+[m[32m            form.save()[m
[32m+[m[32m            return redirect('rmp_bd_app:new_course')[m
[32m+[m[41m            [m
[32m+[m[32m    # Display a blank or invalid form[m
[32m+[m[32m    context = {'form': form, 'courses': courses}[m
[32m+[m[32m    return render(request, 'rmp_bd_app/new_course.html', context)[m
[32m+[m
[32m+[m[32m# /search/?course=[m
[32m+[m[32mdef search_course(request):[m
[32m+[m[32m    course_number = request.GET.get('course')[m
[32m+[m[32m    course_numbers = [][m
[32m+[m[32m    if course_number:[m
[32m+[m[32m        courses = Course.objects.filter(course_number__icontains=course_number)[m
[32m+[m[32m        for course in courses:[m
[32m+[m[32m            course_numbers.append(course.course_title)[m
[32m+[m
[32m+[m[32m    return JsonResponse({'status': 200, 'data' : course_numbers})[m
\ No newline at end of file[m
