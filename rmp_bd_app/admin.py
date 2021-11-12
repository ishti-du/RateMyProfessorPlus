from django.contrib import admin

# Register your models here.
from .models import University
from .models import Campus
from .models import Department
from .models import Professor
from .models import UniversityProfessor
from .models import Course
from .models import Prereq
from .models import Professor_Course
from .models import Review
from .models import Tag
from .models import Review_Tag
from .models import Student_Profile
from .models import Professor_Profile


admin.site.register(University)
admin.site.register(Campus)
admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(UniversityProfessor)
admin.site.register(Course)
admin.site.register(Prereq)
admin.site.register(Professor_Course)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Review_Tag)
admin.site.register(Student_Profile)
admin.site.register(Professor_Profile)

# admin.site.register(Faculty)
# admin.site.register(Feedback)
